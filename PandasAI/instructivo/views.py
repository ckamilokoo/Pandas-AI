from django.shortcuts import render

def instructivo(request):
    return render(request, 'instructivo/instructivo.html')
    # Asegúrate de que 'instructivos.html' sea el nombre de tu plantilla HTML