from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import *
from rest_framework.decorators import api_view
import random 
# Create your views here.
a = 0.001  # Coeficiente da equação (ajustar conforme os dados)
b = 0.0005
c = 10


def calculate_specific_volume(pressure):
    # Implementar a lógica de cálculo com base na equação e nos pontos conhecidos
    # Exemplo simplificado:
    specific_volume = (a * pressure ** 2 + b * pressure + c)
    return specific_volume


@api_view(['GET'])
def index(request):
    try:
        
        return Response({"message": "YetuMusic"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class PhaseChangeDiagramView(APIView):

    def get(self, request):
        pressure = int(request.GET.get("pressure", 1))

        data = {"specific_volume_liquid": 0.0035, "specific_volume_vapor": 0.0035}
        return Response(data, status=status.HTTP_200_OK)

class Status(APIView):

    def get(self, request):
        pressure = int(request.GET.get("pressure", 1))
        systems = sitemDamage.objects.all()
        
        if not systems:
            # Retorna um erro se não houver sistemas cadastrados
            return Response({"error": "No systems found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Escolhe um sistema aleatório da lista
        random_system = random.choice(systems)
        
        
       # Verifica se já existe um seletor ativo e desativa-o
        active_selector = sistemSelector.objects.filter(activo=True).first()
        if active_selector:
            active_selector.activo = False
            active_selector.save()
        
        # Cria e ativa um novo seletor
        new_selector = sistemSelector(sistema=random_system, activo=True)
        new_selector.save()
               
        return Response({ "damaged_system": random_system.name}, status=status.HTTP_200_OK)


class teapot(APIView):

    def post(self, request):

        return Response(status=status.HTTP_418_IM_A_TEAPOT)

class repairBay(APIView):
    def get(self, request):
        # Busca a instância ativa do seletor
        active_selector = sistemSelector.objects.filter(activo=True).first()
        
        if not active_selector:
            return HttpResponse("No active selector found.", status=status.HTTP_404_NOT_FOUND)
        print(active_selector.sistema.name)
        print(active_selector.sistema.value)
        # Renderiza o HTML com os detalhes do seletor ativo
        html_content = render_to_string('index.html', {'selector': active_selector})
        return HttpResponse(html_content)
