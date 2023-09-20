from django.forms import ModelForm
from .models import Scholarships, Announcements


class CreateScholarshipForm(ModelForm):
    class Meta:
        model = Scholarships
        fields = ['name', 'ID', 'description', 'donor',
                  'coverage', 'type', 'requirements']
        
class CreateAnnouncementForm(ModelForm):
    class Meta:
        model = Announcements
        fields = ['id', 'studentId','scholarshipId']
        