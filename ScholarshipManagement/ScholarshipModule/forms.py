from django.forms import ModelForm
from django.forms import Form
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q


class CreateScholarshipForm(ModelForm):


    class Meta:


        model = Scholarships
        fields = [
            'name', 'ID', 'description',
            'donor','coverage', 'type',
            'requirements'
        ]


class CreateNewUser(UserCreationForm):


    username = forms.CharField(
        label='Email', max_length=50, widget=forms.TextInput(attrs={"class":"input"}))
    name = forms.CharField(
        label='Nombre', max_length=20, widget=forms.TextInput(attrs={"class":"input"}))
    password1 = forms.CharField(
        label='Contraseña', widget=forms.PasswordInput(attrs={"class":"input"}))
    password2 = forms.CharField(
        label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={"class":"input"}))
    

    class Meta:


        model = User
        fields = [
            "username",
            "name",
            "password1",
            "password2"
        ]


class Login(AuthenticationForm):


    username = forms.CharField(
        label='Email', max_length=30, widget=forms.TextInput(attrs={"class":"input"}))
    password = forms.CharField(
        label='Contraseña', widget=forms.PasswordInput(attrs={"class":"input"}))
    
    
    class Meta:


        model = User
        fields = [
            "username",
            "password"
        ]

class searchUser(Form):

    username = forms.ModelChoiceField(
        label="Email", queryset= User.objects.filter(~Q(role=0)), initial= 3, widget=forms.Select(attrs={"class":"input"}))
    
class roleAssign(Form):

    CHOICES= (
        (1, 'Asistente de apoyo Financiero'),
        (2, 'Asistente de Filantropía'),
        (3, 'Sin rol')
    )

    role = forms.ChoiceField(
        label="Nuevo rol", choices= CHOICES, initial= 3, widget=forms.Select(attrs={"class":"input"}))