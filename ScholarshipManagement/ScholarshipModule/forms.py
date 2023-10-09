from django.forms import ModelForm
from django.forms.widgets import NumberInput
from django.forms import Form
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q


class CreateScholarshipForm(ModelForm):


    class Meta:


        model = Scholarships
        fields = ['name', 'ID', 'description', 'donor',
                  'coverage', 'type', 'requirements']
        
        
class CreateAnnouncementForm(ModelForm):


    def __init__(self, *args, **kwargs):

        super(CreateAnnouncementForm, self).__init__(*args, **kwargs)
        self.fields['type'].label = "Tipo de convocatoria"


    class Meta:


        model = Announcements
        fields = ['type']


class CreateScholarshipAnnouncementForm(ModelForm):


    scholarshipId = forms.ModelChoiceField(
        label = "ID de la beca", required = True, widget = forms.TextInput(
            attrs = {'cols':'10', "class": "form-control", "placeholder": "123"}), queryset = Scholarships.objects)


    class Meta:


        model = ScholarshipAnnouncements
        fields = ['scholarshipId']


class CreateAnnouncementEventForm(ModelForm):


    def __init__(self, *args, **kwargs):

        super(CreateAnnouncementEventForm, self).__init__(*args, **kwargs)
        self.fields['startingDate'].label = "Fecha de inicio"
        self.fields['endDate'].label = "Fecha de finalización"

    startingDate = forms.DateField(widget = NumberInput(
        attrs = {'type': 'date', "class": "dateInput"}), required=False)
    endDate = forms.DateField(widget=NumberInput(
        attrs = {'type': 'date', "class": "dateInput"}), required=False)


    class Meta:


        model = AnnouncementEvent
        fields = ['startingDate', 'endDate']


class CreateAnnouncementAdditionalEventForm(ModelForm):


    def __init__(self, *args, **kwargs):

        super(CreateAnnouncementAdditionalEventForm, self).__init__(*args, **kwargs)
        self.fields['startingDate'].label = "Fecha de inicio"
        self.fields['endDate'].label = "Fecha de finalización"

    type = forms.CharField(
        label = 'Tipo de convocatoria', max_length=50, required=False, 
        widget = forms.TextInput(attrs = {"class": "additionalItem1"}))
    startingDate = forms.DateField(widget = NumberInput(
        attrs={'type': 'date', "class": "additionalDate"}), required = False)
    endDate = forms.DateField(widget=NumberInput(
        attrs={'type': 'date', "class": "additionalDate"}), required = False)


    class Meta:


        model = AnnouncementEvent
        fields = ['type','startingDate','endDate']


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
        self.fields['name'].widget.attrs['size'] = 35
        self.fields['lastName'].widget.attrs['size'] = 35
        self.fields['studentCode'].widget.attrs['size'] = 35
        self.fields['faculty'].widget.attrs['size'] = 35
        self.fields['major'].widget.attrs['size'] = 35
        self.fields['semester'].widget.attrs['size'] = 35
        self.fields['email'].widget.attrs['size'] = 35
        self.fields['phone'].widget.attrs['size'] = 35
        self.fields['announcement'].widget.attrs['size'] = 35
    
    name = forms.CharField(
        label = "Nombre", max_length = 100, required = True,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'inputForm'}) )
    lastName = forms.CharField(
        label = "Apellido", 
        widget=forms.TextInput(attrs={'placeholder': 'Apellido', 'class': 'inputForm'}))
    studentCode = forms.CharField(
        label = "Código del estudiante", required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Codigo estudiante', 'class': 'inputForm'}))
    faculty = forms.CharField(
        label = "Facultad", required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Facultad', 'class': 'inputForm'}))
    major = forms.CharField(
        label = "Carrera", required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Carrera', 'class': 'inputForm'}))
    semester = forms.IntegerField(
        label = "Semestre", required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'Semestre', 'class': 'inputForm'}))
    email = forms.EmailField(
        label= "Correo electrónico", required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'inputForm'}))
    phone = forms.IntegerField(
        label = "Teléfono", required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Teléfono', 'class': 'inputForm'}))
    status = forms.ChoiceField(
        label="Estado del Estudiante", required=False,
        choices=StatusApplicant.choices, 
        widget=forms.Select(attrs={'class': 'inputForm'}))
    announcement = forms.ModelChoiceField(
        label = "ID de la convocatoria", required=False,
        widget=forms.TextInput(attrs={'cols':'10','placeholder': 'ID convocatoria' , 'class': 'inputForm'} ),queryset=Announcements.objects)


    class Meta:
        model = Applicant
        fields = ['name', 'lastName', 'studentCode',
                  'faculty', 'major', 'semester','email', 'phone','status', 'announcement'] 
        

class FilterApplicantForm(forms.Form):
    ID = forms.CharField(
        label="ID", required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Codigo estudiante', 'class': 'inputForm'}))
    name = forms.CharField(
        label = "Nombre", max_length = 100, required = False,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'inputForm'}) )
    lastName = forms.CharField(
        label = "Apellido", required = False,
        widget=forms.TextInput(attrs={'placeholder': 'Apellido', 'class': 'inputForm'}))
    announcement = forms.ModelChoiceField(
        label = "ID de la convocatoria", required=False,
        widget=forms.TextInput(attrs={'cols':'10','placeholder': 'ID convocatoria' , 'class': 'inputForm'} )
        ,queryset=Announcements.objects)


class AnnouncementAndApplicantForm(forms.ModelForm):
    class Meta:
        model = AnnouncementAndApplicant
        fields = ['announcement', 'applicantID']
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
