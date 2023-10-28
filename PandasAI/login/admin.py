from django.contrib import admin
from django.contrib.auth.models import User  # Importa el modelo de usuario aquí
from .models import CustomUser  # Asegúrate de importar tu modelo de usuario personalizado



admin.site.register(User)  # Registra el modelo de usuario
admin.site.register(CustomUser)  # Registra tu modelo de usuario personalizado
