from django.urls import path
from . import views

urlpatterns = [
    path('subscripcion/', views.subscripcion, name='subscripcion'),
    # Otras rutas de la aplicación
]