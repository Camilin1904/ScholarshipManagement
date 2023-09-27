from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class CreateScholarshipForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(CreateScholarshipForm, self).__init__(*args,**kwargs)
        self.fields['donor'].widget.attrs['size'] = 50
        self.fields['name'].widget.attrs['size'] = 50
        self.fields['ID'].widget.attrs['size'] = 50
        self.fields['description'].widget.attrs['size'] = 50
        self.fields['coverage'].widget.attrs['size'] = 50
        self.fields['type'].widget.attrs['size'] = 50

    donor = forms.ModelChoiceField(
        label = "ID del donante", required=True,
        widget=forms.TextInput(attrs={'cols':'10'}),queryset=Donors.objects)
    name = forms.CharField(
        label = "Nombre", max_length = 100, required = True,
        widget=forms.TextInput())
    description = forms.CharField(
        label = "Descripción", widget=forms.Textarea(attrs={"cols":"104", 'rows':'5'}))
    coverage = forms.CharField(
        label = "Covertura economica", required=True, 
        widget=forms.TextInput())
    type = forms.CharField(
        label = "Tipo", required=True, 
        widget=forms.TextInput())
    requirements = forms.CharField(
        label = "Requerimientos", required=True, 
        widget=forms.Textarea(attrs={'rows':'5'}))
    

    class Meta:


        model = Scholarships
        fields = [
            'name', 'ID', 'description',
            'donor','coverage', 'type',
            'requirements'
        ]


class CreateNewUser(UserCreationForm):


    username = forms.CharField(
        label='Correo', max_length=50, widget=forms.TextInput(attrs={"class":"input"}))
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
        label='Correo', max_length=30, widget=forms.TextInput(attrs={"class":"input"}))
    password = forms.CharField(
        label='Contraseña', widget=forms.PasswordInput(attrs={"class":"input"}))
    
    
    class Meta:


        model = User
        fields = [
            "username",
            "password"
        ]