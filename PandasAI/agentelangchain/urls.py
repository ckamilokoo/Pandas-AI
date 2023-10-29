from django.urls import path
from . import views

urlpatterns = [
    
    path('home_langchain/', views.home_langchain, name='home_langchain'),
    path('agente_langchain/', views.agente_langchain, name='agente_langchain'),
    # Otras rutas de la aplicación
]