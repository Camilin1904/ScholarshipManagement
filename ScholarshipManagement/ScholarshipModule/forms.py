from django.forms import ModelForm
from .models import Scholarships, Announcements, ScholarshipAnnouncements, AnnouncementEvent
from django import forms


class CreateScholarshipForm(ModelForm):
    class Meta:
        model = Scholarships
        fields = ['name', 'ID', 'description', 'donor',
                  'coverage', 'type', 'requirements']
        
class CreateAnnouncementForm(ModelForm):

    class Meta:
        model = Announcements
        fields = ['type']

class CreateScholarshipAnnouncementForm(ModelForm):


    scholarshipId = forms.ModelChoiceField(label = "ID de la beca", required=True,widget=forms.TextInput(attrs={'cols':'10'}),queryset=Scholarships.objects)


    class Meta:
        model = ScholarshipAnnouncements
        fields = ['scholarshipId']


class CreateAnnouncementEventForm(ModelForm):

    startingDate = forms.DateField(widget = forms.SelectDateWidget)
    endDate = forms.DateField(widget = forms.SelectDateWidget)

    class Meta:
        model = AnnouncementEvent
        fields = ['startingDate','endDate']
        