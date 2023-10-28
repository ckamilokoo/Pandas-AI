from django.contrib import admin
from .models import Instruccion
from django.contrib.auth.models import User


# Register your models here.
@admin.register(Instruccion)
class InstruccionAdmin(admin.ModelAdmin):
    list_display = ('titulo', )  # Campos que se mostrarán en la lista de instrucciones

admin.site.register(User)