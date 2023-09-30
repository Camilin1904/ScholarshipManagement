from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


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

class CreateApplicantForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateApplicantForm, self).__init__(*args,**kwargs)
        self.fields['name'].widget.attrs['size'] = 25
        self.fields['lastName'].widget.attrs['size'] = 25
        self.fields['studentCode'].widget.attrs['size'] = 25
        self.fields['faculty'].widget.attrs['size'] = 25
        self.fields['major'].widget.attrs['size'] = 25
        self.fields['semester'].widget.attrs['size'] = 25
        self.fields['email'].widget.attrs['size'] = 25
        self.fields['phone'].widget.attrs['size'] = 25
        self.fields['announcement'].widget.attrs['size'] = 25
    
    name = forms.CharField(
        label = "Nombre", max_length = 100, required = True,
        widget=forms.TextInput())
    lastName = forms.CharField(
        label = "Apellido", 
        widget=forms.TextInput())
    studentCode = forms.CharField(
        label = "Código del estudiante", required=True, 
        widget=forms.TextInput())
    faculty = forms.CharField(
        label = "Facultad", required=True, 
        widget=forms.TextInput())
    major = forms.CharField(
        label = "Carrera", required=True, 
        widget=forms.TextInput())
    semester = forms.IntegerField(
        label = "Semestre", required=True,
        widget=forms.NumberInput())
    email = forms.EmailField(
        label= "Correo electrónico", required=True,
        widget=forms.EmailInput())
    semester = forms.IntegerField(
        label = "Semestre", required=False,
        widget=forms.NumberInput())
    status = forms.ChoiceField(
        label="Estado del Estudiante", required=False,
        choices=StatusApplicant.choices)
    announcement = forms.ModelChoiceField(
        label = "ID de la convocatoria", required=False,
        widget=forms.TextInput(attrs={'cols':'10'}),queryset=Announcement.objects)

    


    class Meta:
        model = Applicant
        fields = ['name', 'lastName', 'studentCode',
                  'faculty', 'major', 'semester','email', 'phone','status', 'announcement'] 