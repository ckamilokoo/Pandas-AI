from django.contrib import admin
from .models import Instruccion


# Register your models here.
@admin.register(Instruccion)
class InstruccionAdmin(admin.ModelAdmin):
    list_display = ('titulo', )  # Campos que se mostrarán en la lista de instrucciones