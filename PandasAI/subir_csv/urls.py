from django.urls import path
from . import views

urlpatterns = [
    path('subir_csv/', views.subir_csv, name='subir_csv'),
    # Otras rutas de la aplicación
]