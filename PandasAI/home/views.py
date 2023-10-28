from django.shortcuts import get_object_or_404, redirect, render

from .models import Publicacion
from .forms import PublicacionForm  # Asegúrate de tener el formulario definido en forms.py

# Create your views here.

#función para ver la página home 
#publicaciones crud

def home(request):
    publicaciones = Publicacion.objects.all()
    
    return render(request, 'home/home.html', {'publicaciones': publicaciones})

def crear_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_publicacion')  # Redirige a la vista de listar publicaciones
    else:
        form = PublicacionForm()

    return render(request, 'home/publicacion/crear_publicacion.html', {'form': form})

def actualizar_publicacion(request, publicacion_id):
    publicacion = get_object_or_404(Publicacion, pk=publicacion_id)
    
    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES, instance=publicacion)
        if form.is_valid():
            form.save()
            return redirect('listar_publicacion')  # Redirige a la vista de listar publicaciones
    else:
        form = PublicacionForm(instance=publicacion)

    return render(request, 'home/publicacion/actualizar_publicacion.html', {'form': form, 'publicacion': publicacion})

def listar_publicacion(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'home/publicacion/listar_publicacion.html', {'publicaciones': publicaciones})

def eliminar_publicacion(request, publicacion_id):
    if request.method == 'POST':
        publicacion = get_object_or_404(Publicacion, pk=publicacion_id)
        publicacion.delete()
        return redirect('listar_publicacion')  # Redirige a la vista de listado de publicaciones
    else:
        # Maneja posibles solicitudes GET de forma adecuada (puedes mostrar un mensaje o redirigir a otra página).
        pass
    
#
