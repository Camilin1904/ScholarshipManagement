from django.forms import ModelForm
from .models import Scholarships, Announcements, ScholarshipAnnouncements, AnnouncementEvent
from django import forms
from django.forms.widgets import NumberInput


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


    scholarshipId = forms.ModelChoiceField(label = "ID de la beca", required=True,widget=forms.TextInput(attrs={'cols':'10', "class": "form-control", "placeholder":"123"}),queryset=Scholarships.objects)

    class Meta:
        model = ScholarshipAnnouncements
        fields = ['scholarshipId']


class CreateAnnouncementEventForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(CreateAnnouncementEventForm, self).__init__(*args, **kwargs)
        self.fields['startingDate'].label = "Fecha de inicio"
        self.fields['endDate'].label = "Fecha de finalización"

    startingDate = forms.DateField(widget=NumberInput(attrs={'type': 'date', "class": "dateInput"}),required=False)
    endDate = forms.DateField(widget=NumberInput(attrs={'type': 'date', "class": "dateInput"}),required=False)

    class Meta:
        model = AnnouncementEvent
        fields = ['startingDate','endDate']



class CreateAnnouncementAdditionalEventForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(CreateAnnouncementAdditionalEventForm, self).__init__(*args, **kwargs)
        self.fields['startingDate'].label = "Fecha de inicio"
        self.fields['endDate'].label = "Fecha de finalización"

    type = forms.CharField(label='Tipo de convocatoria', max_length=50, required=False, widget=forms.TextInput(attrs={"class": "additionalItem1"}))

    startingDate = forms.DateField(widget=NumberInput(attrs={'type': 'date', "class": "additionalDate"}),required=False)
    endDate = forms.DateField(widget=NumberInput(attrs={'type': 'date', "class": "additionalDate"}),required=False)

    class Meta:
        model = AnnouncementEvent
        fields = ['type','startingDate','endDate']
        