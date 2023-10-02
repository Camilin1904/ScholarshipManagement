from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class CreateScholarshipForm(ModelForm):
    
    #def __init__(self, *args, **kwargs):
        #super(CreateScholarshipForm, self).__init__(*args,**kwargs)
        #self.fields['donor'].widget.attrs['size'] = 51
        #self.fields['name'].widget.attrs['size'] = 51
        #self.fields['ID'].widget.attrs['size'] = 51
        #self.fields['description'].widget.attrs['size'] = 50
        #self.fields['coverage'].widget.attrs['size'] = 51
        #self.fields['type'].widget.attrs['size'] = 3

    donor = forms.ModelChoiceField(
        label = "ID del donante", required=True,
        widget=forms.TextInput(attrs={"class":"id_donor"}),queryset=Donors.objects)
    name = forms.CharField(
        label = "Nombre", max_length = 100, required = True,
        widget=forms.TextInput(attrs={"class":"id_name"}))
    description = forms.CharField(
        label = "Descripción", widget=forms.Textarea(attrs={"class":"id_description",'rows':'3'}))
    coverage = forms.CharField(
        label = "Covertura economica", required=True, 
        widget=forms.TextInput(attrs={"class":"id_coverage"}))
    type = forms.CharField(
        label = "Tipo", required=True, 
        widget=forms.RadioSelect(choices=Scholarships.ScholarshipType.choices, attrs={'size':'3'}))
    requirements = forms.CharField(
        label = "Requerimientos",
        widget=forms.Textarea(attrs={"class":"id_requirements",'rows':'3'}))
    ID = forms.IntegerField(label = 'ID', required=True, widget=forms.TextInput(attrs={"class":"id_ID"}))
    

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