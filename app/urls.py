from django.urls import  path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("phase-change-diagram", PhaseChangeDiagramView.as_view(), name="index"),

]