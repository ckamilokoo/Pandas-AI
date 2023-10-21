from django import forms
from .models import CustomUser

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'nivel']

    nivel = forms.ChoiceField(choices=CustomUser.NIVEL_CHOICES)