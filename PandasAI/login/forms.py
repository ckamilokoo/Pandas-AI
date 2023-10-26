from django import forms
from login.models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    NIVEL_CHOICES = (
        (1, 'Usuario Normal'),
        (2, 'Usuario con Subscripción A'),
        (3, 'Usuario con Subscripción B'),
    )

    nivel = forms.ChoiceField(choices=NIVEL_CHOICES, label='Nivel', initial=1)  # Establece 'Usuario Normal' como predeterminado

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'nivel']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.nivel = self.cleaned_data['nivel']
        if commit:
            user.save()
        return user

