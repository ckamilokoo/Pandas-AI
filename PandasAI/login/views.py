from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login ,logout 
from django.http import HttpResponseBadRequest 
from django.views.generic import View 
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm 
from django.shortcuts import render, redirect 
from django.contrib import messages  

class Vregistro(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'login/registro.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            nivel = form.cleaned_data.get('nivel')  # Obtén el nivel del formulario
            user = form.save()
            user.nivel = nivel  # Asigna el nivel al usuario
            user.save()

            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect("home")
        else:
            return render(request, 'login/registro.html', {'form': form})


def cerrar_sesion(request):
        logout(request)
        return redirect("home")

def iniciar_sesion(request):     
    if request.method=="POST":         
        form=AuthenticationForm(request.POST, data=request.POST)         
        if form.is_valid():             
            nombre_usuario=form.cleaned_data.get("username")             
            contra=form.cleaned_data.get("password")             
            usuario=authenticate(username=nombre_usuario,password=contra)             
            if usuario is not None:                 
                login(request,usuario)                 
                return redirect("home")             
            else:                 
                messages.error(request, "usuario no valido ")         
        else:             
            messages.error(request , "informacion incorrecta")                      
    form=AuthenticationForm()     
    return render(request,"login/login.html",{"form":form})