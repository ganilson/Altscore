from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.decorators import api_view

# Create your views here.
a = 0.001  # Coeficiente da equação (ajustar conforme os dados)
b = 0.0005
c = 10

def calculate_specific_volume(pressure):
    # Implementar a lógica de cálculo com base na equação e nos pontos conhecidos
    # Exemplo simplificado:
    specific_volume =(a * pressure**2 + b * pressure + c)
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
