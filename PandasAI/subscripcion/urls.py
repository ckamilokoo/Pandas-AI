# En nivel_usuario/urls.py

from django.urls import path
from . import views

app_name = 'nivel_usuario'

urlpatterns = [
    # Ruta para actualizar al nivel 2
    path('actualizar_nivel/2/', views.actualizar_nivel, {'nuevo_nivel': 2}, name='actualizar_nivel_2'),
    
    # Ruta para actualizar al nivel 3
    path('actualizar_nivel/3/', views.actualizar_nivel, {'nuevo_nivel': 3}, name='actualizar_nivel_3'),
]
