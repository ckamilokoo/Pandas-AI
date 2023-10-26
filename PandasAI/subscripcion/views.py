from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from login.models import CustomUser
from django.contrib import messages
from django.shortcuts import redirect

@login_required
def actualizar_nivel(request, nuevo_nivel):
    # Obtén el usuario actual
    user = request.user

    # Verifica si el usuario es un usuario normal y el nuevo nivel es válido
    if user.nivel == 1 and nuevo_nivel in [2, 3]:
        user.nivel = nuevo_nivel
        user.save()
        messages.success(request, f"Tu nivel se ha actualizado a Nivel {nuevo_nivel}.")
    elif user.nivel in [2, 3] and nuevo_nivel == 1:
        user.nivel = nuevo_nivel
        user.save()
        messages.success(request, "Tu nivel se ha actualizado a Usuario Normal.")
    else:
        messages.error(request, "No puedes actualizar tu nivel en este momento.")

    return redirect('home')


@login_required
def cancelar_nivel(request):
    # Obtén el usuario actual
    user = request.user

    # Verifica si el usuario tiene un nivel superior a Usuario Normal
    if user.nivel in [2, 3]:
        user.nivel = 1
        user.save()
        messages.success(request, "Tu nivel se ha actualizado a Usuario Normal.")
    else:
        messages.error(request, "No puedes cancelar tu nivel en este momento.")

    return redirect('home')







# Create your views here.
def subscripcion(request):
    return render(request, 'subscripcion/subscripcion.html')

