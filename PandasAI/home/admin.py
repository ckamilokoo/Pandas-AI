from django.contrib import admin
from .models import Publicacion
from django.contrib import admin
from django.contrib.auth.models import User  # Importa el modelo de usuario aquí




# Register your models here.


admin.site.register(Publicacion)
admin.site.register(User)  # Registra el modelo de usuario