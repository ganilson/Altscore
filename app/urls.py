from django.urls import  path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("status", Status.as_view(), name="index"),
    path("repair-bay", repairBay.as_view(), name="repairBay"),
    path("teapot", teapot.as_view(), name="index"),
    path("phase-change-diagram", PhaseChangeDiagramView.as_view(), name="index"),
    
]