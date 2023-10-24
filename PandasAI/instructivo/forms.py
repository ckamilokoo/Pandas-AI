from django import forms
from .models import Instruccion  # Asegúrate de importar tu modelo

class InstruccionForm(forms.ModelForm):
    class Meta:
        model = Instruccion  # Especifica el modelo asociado
        fields = ['titulo', 'contenido']  # Lista de campos a incluir en el formulario
