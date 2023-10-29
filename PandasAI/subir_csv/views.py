from django.shortcuts import render
from .forms import CSVUploadForm
from django.conf import settings
import os

def subir_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Procesar el archivo CSV aquí si es necesario
            archivo_csv = form.cleaned_data['archivo_csv']
            
            # Define la ubicación donde se guardará el archivo CSV
            archivo_ruta = os.path.join(settings.MEDIA_ROOT, 'csv', archivo_csv.name)
            
            # Guarda el archivo en la ubicación especificada
            with open(archivo_ruta, 'wb+') as destination:
                for chunk in archivo_csv.chunks():
                    destination.write(chunk)
            
            # Luego, puedes renderizar una página de éxito o redirigir a otra vista
            return render(request, 'subir_csv/subir_csv.html', {'archivo_csv': archivo_csv})
    else:
        form = CSVUploadForm()

    return render(request, 'subir_csv/subir_csv.html', {'form': form})
