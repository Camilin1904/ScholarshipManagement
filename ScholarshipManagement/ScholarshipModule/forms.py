from django.forms import ModelForm
from django import forms
from .models import Scholarships


class CreateScholarshipForm(ModelForm):
    class Meta:
        model = Scholarships
        fields = ['name', 'ID', 'description', 'donor',
                  'coverage', 'type', 'requirements']

class CreateNewUser(forms.Form):
    id = forms.CharField(label='Usuario', max_length=30, widget=forms.TextInput(attrs={"class":"input"}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={"class":"input"}))
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={"class":"input"}))

class Login(forms.Form):
    id = forms.CharField(label='Usuario', max_length=30, widget=forms.TextInput(attrs={"class":"input"}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={"class":"input"}))
