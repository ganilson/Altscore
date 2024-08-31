from django.urls import  path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("phase-change-diagram", phase_phase_change_diagram, name="index"),

]