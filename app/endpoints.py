# views.py
from rest_framework import generics
from .models import Inscricao
from .serializers import InscricaoSerializer
from utils.senders import *
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.exceptions import ValidationError
from django.db import transaction
from smtplib import SMTPException

import traceback
class InscricaoListCreateView(generics.ListCreateAPIView):
    queryset = Inscricao.objects.all()
    serializer_class = InscricaoSerializer

    def perform_create(self, serializer):
        # Obtém o e-mail da inscrição sendo criada
        email = serializer.validated_data.get('email')
        
        # Verifica se o e-mail já está registrado
        if Inscricao.objects.filter(email=email).exists():
            raise AuthenticationFailed({"email": "Este e-mail já foi inscrito. Por favor, use outro e-mail."})

        # Utiliza uma transação para garantir a atomicidade
        with transaction.atomic():
            # Salva a inscrição no banco de dados
            instance = serializer.save()

            # Envia o e-mail de confirmação após a criação da inscrição
            try:
                sendEmail(
                    instance.email,
                    'Confirmação de Inscrição',
                    'welcome.html',
                    context={'inscricao': instance}
                )
            except SMTPException as smtp_error:
                print(f"Erro de SMTP: {smtp_error}")
                raise ValidationError({"email": "Falha ao enviar e-mail. Tente novamente mais tarde."})
            except Exception as e:
                print(f"Erro inesperado: {e}")
                raise ValidationError({"email": "Falha ao enviar e-mail. Tente novamente mais tarde."})