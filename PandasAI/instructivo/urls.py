from django.urls import path
from . import views

urlpatterns = [
    path('instructivo/', views.instructivo, name='instructivo'),
    # Agrega más rutas según sea necesario
]