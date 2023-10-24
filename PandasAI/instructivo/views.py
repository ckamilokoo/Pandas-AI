from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .forms import InstruccionForm
from .models import Instruccion

def instructivo(request):
    return render(request, 'instructivo/instructivo.html')
    # Asegúrate de que 'instructivos.html' sea el nombre de tu plantilla HTML

class InstruccionCreateView(CreateView):
    model = Instruccion
    form_class = InstruccionForm
    template_name = 'instructivo/crear_instruccion.html'
    success_url = reverse_lazy('listar_instrucciones')

class InstruccionUpdateView(UpdateView):
    model = Instruccion
    form_class = InstruccionForm
    template_name = 'instructivo/editar_instruccion.html'
    success_url = reverse_lazy('listar_instrucciones')

class InstruccionDeleteView(DeleteView):
    model = Instruccion
    template_name = 'instructivo/eliminar_instruccion.html'
    success_url = reverse_lazy('listar_instrucciones')

class InstruccionListView(ListView):
    model = Instruccion
    template_name = 'instructivo/instructivo.html'