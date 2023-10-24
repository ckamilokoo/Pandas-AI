from django.urls import path
from . import views
from .views import InstruccionCreateView, InstruccionUpdateView, InstruccionDeleteView, InstruccionListView

urlpatterns = [
    path('instructivo/', views.instructivo, name='instructivo'),
    path('instrucciones/', InstruccionListView.as_view(), name='listar_instrucciones'),
    path('instrucciones/crear/', InstruccionCreateView.as_view(), name='crear_instruccion'),
    path('instrucciones/editar/<int:pk>/', InstruccionUpdateView.as_view(), name='editar_instruccion'),
    path('instrucciones/eliminar/<int:pk>/', InstruccionDeleteView.as_view(), name='eliminar_instruccion'),
]