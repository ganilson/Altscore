from rest_framework import serializers
from .models import Inscricao

class InscricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscricao
        fields = '__all__'
        extra_kwargs = {
            'email': {'required': True}
        }
