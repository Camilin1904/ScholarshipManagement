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


    scholarshipId = forms.ModelChoiceField(label = "ID de la beca", required=True,widget=forms.TextInput(attrs={'cols':'10', "class": "form-control", "placeholder":"Id Beca"}),queryset=Scholarships.objects)

    class Meta:
        model = ScholarshipAnnouncements
        fields = ['scholarshipId']


class CreateAnnouncementEventForm(ModelForm):

    startingDate = forms.DateField(widget = forms.SelectDateWidget(attrs={"class": "form-control"}))
    endDate = forms.DateField(widget = forms.SelectDateWidget(attrs={"class": "form-control"}))

    class Meta:
        model = AnnouncementEvent
        fields = ['startingDate','endDate']



class CreateAnnouncementAdditionalEventForm(ModelForm):

    type = forms.CharField(label='eventType', max_length=50, required=False, widget=forms.TextInput(attrs={"class": "additionalItem1"}))

    startingDate = forms.DateField(widget = forms.SelectDateWidget(attrs={"class": "additionalItem2"}))
    endDate = forms.DateField(widget = forms.SelectDateWidget(attrs={"class": "additionalItem3"}))  

    class Meta:
        model = AnnouncementEvent
        fields = ['type','startingDate','endDate']
        