from django import forms

class CSVUploadForm(forms.Form):
    archivo_csv = forms.FileField(
        label='Selecciona un archivo CSV',
        help_text='El archivo debe ser de tipo CSV.'
    )

    def clean_archivo_csv(self):
        archivo = self.cleaned_data.get('archivo_csv')
        if archivo:
            # Valida que el archivo tenga una extensión .csv
            if not archivo.name.endswith('.csv'):
                raise forms.ValidationError('El archivo debe tener la extensión .csv')
        return archivo