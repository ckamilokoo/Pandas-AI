from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Asocia la vista 'home' a la URL raíz
]
