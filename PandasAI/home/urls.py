from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Asocia la vista 'home' a la URL raíz
    path('crear_publicacion', views.crear_publicacion, name='crear_publicacion'),
    path('listar_publicacion/', views.listar_publicacion, name='listar_publicacion'),
    path('eliminar_publicacion/<int:publicacion_id>/', views.eliminar_publicacion, name='eliminar_publicacion'),
    path('actualizar_publicacion/<int:publicacion_id>/', views.actualizar_publicacion, name='actualizar_publicacion'),
    
]
