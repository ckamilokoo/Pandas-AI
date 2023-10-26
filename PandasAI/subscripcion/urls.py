from django.urls import path
from . import views

urlpatterns = [
    path('subscripcion/', views.subscripcion, name='subscripcion'),
    path('actualizar-nivel/<int:nuevo_nivel>/', views.actualizar_nivel, name='actualizar_nivel'),
    # Otras rutas de la aplicación
    path('cancelar-nivel/', views.cancelar_nivel, name='cancelar_nivel'),
]