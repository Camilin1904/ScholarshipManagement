from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class CreateScholarshipForm(ModelForm):
    class Meta:
        model = Scholarships
        fields = ['name', 'ID', 'description', 'donor',
                  'coverage', 'type', 'requirements']

class CreateNewUser(UserCreationForm):
    username = forms.CharField(label='Correo', max_length=50, widget=forms.TextInput(attrs={"class":"input"}))
    name = forms.CharField(label='Nombre', max_length=20, widget=forms.TextInput(attrs={"class":"input"}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={"class":"input"}))
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={"class":"input"}))
    class Meta:
        model = User
        fields = ["username", "name", "password1", "password2"]

class Login(AuthenticationForm):
    username = forms.CharField(label='Correo', max_length=30, widget=forms.TextInput(attrs={"class":"input"}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={"class":"input"}))
    class Meta:
        model = User
        fields = ["username", "password"]