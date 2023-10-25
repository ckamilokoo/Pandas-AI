from django.shortcuts import render

# Create your views here.
def subscripcion(request):
    return render(request, 'subscripcion/subscripcion.html')