from django.forms import ModelForm
from .models import Scholarships, Announcements, ScholarshipAnnouncements
from django import forms


class CreateScholarshipForm(ModelForm):
    class Meta:
        model = Scholarships
        fields = ['name', 'ID', 'description', 'donor',
                  'coverage', 'type', 'requirements']
        
class CreateAnnouncementForm(ModelForm):

    scholarshipID = forms.CharField(
        label='Código del programa de beca', max_length=50, widget=forms.TextInput(attrs={"class":"input"}))
    
    inscriptionStart = forms.DateField(
        label='Inicio de inscripciones', max_length=50, widget=forms.DateInput(attrs={"class":"input"}))    

    class Meta:
        model = Announcements
        fields = ['Type']

    class Meta:
        model = ScholarshipAnnouncements
        fields = ['scholarshipId']

        