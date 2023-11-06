from django.forms import ModelForm
from django.forms.widgets import NumberInput
from django.forms import Form
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q


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
    type = forms.IntegerField(
        label = "Tipo", required=True, 
        widget=forms.RadioSelect(choices=Scholarships.ScholarshipType.choices, attrs={'size':'3'}))
    requirements = forms.CharField(
        label = "Requerimientos",
        widget=forms.Textarea(attrs={"class":"id_requirements",'rows':'3'}))
    ID = forms.IntegerField(label = 'ID', required=True, widget=forms.TextInput(attrs={"class":"id_ID"}))
    

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


    def __init__(
        self, *args, **kwargs):

        super(CreateApplicantForm, self).__init__(*args,**kwargs)
        self.fields['name'].widget.attrs['size'] = 35
        self.fields['lastName'].widget.attrs['size'] = 35
        self.fields['studentCode'].widget.attrs['size'] = 1
        self.fields['faculty'].widget.attrs['size'] = 1
        self.fields['major'].widget.attrs['size'] = 1
        self.fields['semester'].widget.attrs['size'] = 1
        self.fields['email'].widget.attrs['size'] = 35
        self.fields['phone'].widget.attrs['size'] = 35
        self.fields['announcement'].widget.attrs['size'] = 35
    

    CAREER_CHOICES = (
        ("Administración de Empresas", "Administración de Empresas"),
        ("Antropología", "Antropología"),
        ("Biología", "Biología"),
        ("Ciencia Política", "Ciencia Política"),
        ("Comunicación", "Comunicación"),
        ("Derecho", "Derecho"),
        ("Diseño de Medios Interactivos", "Diseño de Medios Interactivos"),
        ("Diseño Industrial", "Diseño Industrial"),
        ("Economía y Negocios Internacionales", "Economía y Negocios Internacionales"),
        ("Finanzas", "Finanzas"),
        ("Ingeniería Bioquímica", "Ingeniería Bioquímica"),
        ("Ingeniería de Sistemas", "Ingeniería de Sistemas"),
        ("Ingeniería Industrial", "Ingeniería Industrial"),
        ("Ingeniería Telemática", "Ingeniería Telemática"),
        ("Licenciatura en Artes", "Licenciatura en Artes"),
        ("Licenciatura en Ciencias Naturales", "Licenciatura en Ciencias Naturales"),
        ("Licenciatura en Ciencias Sociales", "Licenciatura en Ciencias Sociales"),
        ("Licenciatura en Educación Básica Primaria", "Licenciatura en Educación Básica Primaria"),
        ("Licenciatura en Lenguas Extranjeras", "Licenciatura en Lenguas Extranjeras"),
        ("Licenciatura en Literatura y Lengua Castellana", "Licenciatura en Literatura y Lengua Castellana"),
        ("Medicina", "Medicina"),
        ("Mercadeo Internacional y Publicidad", "Mercadeo Internacional y Publicidad"),
        ("Música", "Música"),
        ("Psicología", "Psicología"),
        ("Química con Énfasis en Bioquímica", "Química con Énfasis en Bioquímica"),
        ("Química Farmacéutica", "Química Farmacéutica"),
        ("Sociología", "Sociología")
    )

    FACULTY_CHOICES = (
        ("Ciencias Administrativas y Económicas", "Ciencias Administrativas y Económicas"),
        ("Ciencias Humanas", "Ciencias Humanas"),
        ("Ingeniería, Diseño y Ciencias Aplicadas", "Ingeniería, Diseño y Ciencias Aplicadas"),
        ("Ciencias de la Salud", "Ciencias de la Salud")
    )

    SEMESTER_CHOICES = (
        ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5","5"), ("6","6"), 
        ("7", "7"), ("8", "8"), ("9", "9"), ("10", "10"), ("11", "11"), ("12", "12")
        )
    

    name = forms.CharField(
        label = "Nombre", max_length = 100, required = True,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'inputForm'}))
    lastName = forms.CharField(
        label = "Apellido", max_length = 100, required = True,
        widget=forms.TextInput(attrs={'placeholder': 'Apellido', 'class': 'inputForm'}))
    studentCode = forms.CharField(
        label = "Código del estudiante", required=True, widget=forms.TextInput(
            attrs={'placeholder': 'Codigo estudiante', 'class': 'inputForm'}))
    faculty = forms.ChoiceField(
        label = "Facultad", required=True, choices = FACULTY_CHOICES,
        widget=forms.Select(
            attrs={'class': 'inputForm'}))
    major = forms.ChoiceField(
        label = "Carrera", required=True, choices = CAREER_CHOICES,
        widget=forms.Select(attrs={'class': 'inputForm'}))
    semester = forms.ChoiceField(
        label = "Semestre", required=True, choices = SEMESTER_CHOICES,
        widget=forms.Select(
            attrs={'class': 'inputForm'}))
    email = forms.EmailField(
        label= "Correo electrónico", required=True, widget=forms.EmailInput(
            attrs={'placeholder': 'Email', 'class': 'inputForm'}))
    phone = forms.CharField(
        label = "Teléfono", required=False, widget=forms.TextInput(
            attrs={'placeholder': 'Teléfono', 'class': 'inputForm'}))
    status = forms.ChoiceField(
        label="Estado del Estudiante", required=False, choices=StatusApplicant.choices, 
        widget=forms.Select(attrs={'class': 'inputForm'}))
    announcement = forms.ModelChoiceField(
        label = "ID de la convocatoria", required=False,widget=forms.TextInput(
            attrs={'cols':'10','placeholder': 'ID convocatoria', 'class': 'inputForm'}),
        queryset=Announcements.objects) 
    image = forms.ImageField(
        label="Subir imagen", required=False,
        widget=forms.FileInput(attrs={'class': 'inputForm', 'placeholder': 'Seleccionar imagen'}))
    
    class Meta:


        model = Applicant
        fields = [
            'name', 'lastName', 'studentCode',
            'faculty', 'major', 'semester',
            'email','phone','status', 
            'announcement','image'
        ] 
 

        
class CreateAppliStep1Form(forms.Form):


    def __init__(
        self, *args, **kwargs):

        super(CreateAppliStep1Form, self).__init__(*args,**kwargs)
        self.fields['name'].widget.attrs['size'] = 35
        self.fields['lastName'].widget.attrs['size'] = 35
        self.fields['email'].widget.attrs['size'] = 35
        self.fields['phone'].widget.attrs['size'] = 35
       
    
    name = forms.CharField(
        label = "Nombre", max_length = 100, required = True,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'inputForm'}))
    lastName = forms.CharField(
        label = "Apellido", max_length = 100, required = True,
        widget=forms.TextInput(attrs={'placeholder': 'Apellido', 'class': 'inputForm'}))
    email = forms.EmailField(
        label= "Correo electrónico", required=True, widget=forms.EmailInput(
            attrs={'placeholder': 'Email', 'class': 'inputForm'}))
    phone = forms.CharField(
        label = "Teléfono", required=False, widget=forms.TextInput(
            attrs={'placeholder': 'Teléfono', 'class': 'inputForm'}))
    image = forms.ImageField(
        label="Subir imagen", required=False,
        widget=forms.FileInput(attrs={'class': 'inputForm', 'placeholder': 'Seleccionar imagen'}))
    

    class Meta:

        model = Applicant
        fields = [
            'name', 'lastName', 'email',
            'phone', 'image'
        ]



class CreateAppliStep2Form(forms.Form):  


    def __init__(
        self, *args, **kwargs):

        super(CreateAppliStep2Form, self).__init__(*args,**kwargs)
        self.fields['studentCode'].widget.attrs['size'] = 1
        self.fields['faculty'].widget.attrs['size'] = 1
        self.fields['major'].widget.attrs['size'] = 1
        self.fields['semester'].widget.attrs['size'] = 1


    CAREER_CHOICES = (
        ("Administración de Empresas", "Administración de Empresas"),
        ("Antropología", "Antropología"),
        ("Biología", "Biología"),
        ("Ciencia Política", "Ciencia Política"),
        ("Comunicación", "Comunicación"),
        ("Derecho", "Derecho"),
        ("Diseño de Medios Interactivos", "Diseño de Medios Interactivos"),
        ("Diseño Industrial", "Diseño Industrial"),
        ("Economía y Negocios Internacionales", "Economía y Negocios Internacionales"),
        ("Finanzas", "Finanzas"),
        ("Ingeniería Bioquímica", "Ingeniería Bioquímica"),
        ("Ingeniería de Sistemas", "Ingeniería de Sistemas"),
        ("Ingeniería Industrial", "Ingeniería Industrial"),
        ("Ingeniería Telemática", "Ingeniería Telemática"),
        ("Licenciatura en Artes", "Licenciatura en Artes"),
        ("Licenciatura en Ciencias Naturales", "Licenciatura en Ciencias Naturales"),
        ("Licenciatura en Ciencias Sociales", "Licenciatura en Ciencias Sociales"),
        ("Licenciatura en Educación Básica Primaria", "Licenciatura en Educación Básica Primaria"),
        ("Licenciatura en Lenguas Extranjeras", "Licenciatura en Lenguas Extranjeras"),
        ("Licenciatura en Literatura y Lengua Castellana", "Licenciatura en Literatura y Lengua Castellana"),
        ("Medicina", "Medicina"),
        ("Mercadeo Internacional y Publicidad", "Mercadeo Internacional y Publicidad"),
        ("Música", "Música"),
        ("Psicología", "Psicología"),
        ("Química con Énfasis en Bioquímica", "Química con Énfasis en Bioquímica"),
        ("Química Farmacéutica", "Química Farmacéutica"),
        ("Sociología", "Sociología")
    )

    FACULTY_CHOICES = (
        ("Ciencias Administrativas y Económicas", "Ciencias Administrativas y Económicas"),
        ("Ciencias Humanas", "Ciencias Humanas"),
        ("Ingeniería, Diseño y Ciencias Aplicadas", "Ingeniería, Diseño y Ciencias Aplicadas"),
        ("Ciencias de la Salud", "Ciencias de la Salud")
    )

    SEMESTER_CHOICES = (
        ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5","5"), ("6","6"), 
        ("7", "7"), ("8", "8"), ("9", "9"), ("10", "10"), ("11", "11"), ("12", "12")
        )


    studentCode = forms.CharField(
        label = "Código del estudiante", required=True, widget=forms.TextInput(
            attrs={'placeholder': 'Codigo estudiante', 'class': 'inputForm'}))
    faculty = forms.ChoiceField(
        label = "Facultad", required=True, choices = FACULTY_CHOICES,
        widget=forms.Select(
            attrs={'class': 'inputForm'}))
    major = forms.ChoiceField(
        label = "Carrera", required=True, choices = CAREER_CHOICES,
        widget=forms.Select(attrs={'class': 'inputForm'}))
    semester = forms.ChoiceField(
        label = "Semestre", required=True, choices = SEMESTER_CHOICES,
        widget=forms.Select(
            attrs={'class': 'inputForm'}))

    class Meta:


        fields = [
            'studentCode', 'faculty', 'major', 
            'semester', 
        ] 

class FilterApplicantForm(forms.Form):


    ID = forms.CharField(
        label="ID", required=False, widget=forms.TextInput(
            attrs={'placeholder': 'Codigo estudiante', 'class': 'inputForm'}))
    name = forms.CharField(
        label = "Nombre", max_length = 100, required = False,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'inputForm'}))
    lastName = forms.CharField(
        label = "Apellido", required = False,
        widget=forms.TextInput(attrs={'placeholder': 'Apellido', 'class': 'inputForm'}))
    announcement = forms.ModelChoiceField(
        label = "ID de la convocatoria", required=False, widget=forms.TextInput(
            attrs={'cols':'10','placeholder': 'ID convocatoria' , 'class': 'inputForm'}),
        queryset=Announcements.objects)

class FilterScholarshipForm(forms.Form):
    donor = forms.ModelChoiceField(
        label = "ID del donante", required=False,
        widget=forms.TextInput(attrs={"class":"id_donor"}),queryset=Donors.objects)
    name = forms.CharField(
        label = "Nombre", max_length = 100, required = False,
        widget=forms.TextInput(attrs={"class":"id_name"}))
    minCoverage = forms.CharField(
        label = "Covertura economica minima", required=False, 
        widget=forms.TextInput(attrs={"class":"id_coverage"}))
    maxCoverage = forms.CharField(
        label = "Covertura economica maxima", required=False, 
        widget=forms.TextInput(attrs={"class":"id_coverage"}))
    type = forms.IntegerField(
        label = "Tipo", required=False, 
        widget=forms.CheckboxSelectMultiple(choices=Scholarships.ScholarshipType.choices, attrs={'size':'3'}))

class AnnouncementAndApplicantForm(forms.ModelForm):


    class Meta:


        model = AnnouncementAndApplicant
        fields = [
            'announcement', 'applicant'
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
    
class CreateSearchAnnouncementForm(forms.Form):

    def __init__(self, *args, **kwargs):

        super(CreateSearchAnnouncementForm, self).__init__(*args, **kwargs)
        self.fields['scholarshipName'].label = "Nombre la beca"
        self.fields['announcementId'].label = "ID de la convocatoria"
        self.fields['announcementType'].label = "Tipo de convocatoria"
        self.fields['announcementStatus'].label = "Estado de la convocatoria"
        self.fields['startingInscriptionDate'].label = "Fecha inicial"
        self.fields['endInscriptionDate'].label = "Fecha final"

    TYPE_CHOICES = ( 
    ("3", ""),
    ("0", "Abierta"), 
    ("1", "Cerrada"), 
    ("2", "Mixta"), 
    )

    STATUS_CHOICES = ( 
    ("2", ""),
    ("0", "Activa"), 
    ("1", "Inactiva"), 
    )

    scholarshipName = forms.CharField( max_length=100, widget = forms.TextInput(
            attrs = { "class": "searchform"}), required=False) 
    announcementId = forms.CharField( max_length=100, widget = forms.TextInput(
            attrs = { "class": "searchform"}), required=False)
    announcementType = forms.ChoiceField(choices = TYPE_CHOICES,required=False)
    announcementStatus = forms.ChoiceField(choices = STATUS_CHOICES,required=False)
    startingInscriptionDate = forms.DateField(widget = NumberInput(
        attrs={'type': 'date', "class": "searchform"}), required = False)
    endInscriptionDate = forms.DateField(widget = NumberInput(
        attrs={'type': 'date', "class": "searchform"}), required = False)


