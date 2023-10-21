# En views.py de la nueva aplicación
from django.shortcuts import redirect
from login.models import CustomUser

def actualizar_nivel(request, nuevo_nivel):
    if request.user.is_authenticated:
        try:
            user = CustomUser.objects.get(pk=request.user.pk)
            user.nivel = nuevo_nivel
            user.save()
            return redirect("home")  # Redirige a la página de inicio o a donde desees
        except CustomUser.DoesNotExist:
            # Maneja el caso si el usuario no existe en la base de datos
            pass
    return redirect("home")








# Create your views here.
