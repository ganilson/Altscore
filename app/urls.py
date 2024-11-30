from django.urls import path
from .views import *
from  .endpoints import *
urlpatterns = [
    path('',  index, name="home" ),
    path('inscricao',  InscricaoListCreateView.as_view(), name="inscricao" ),
    
]
