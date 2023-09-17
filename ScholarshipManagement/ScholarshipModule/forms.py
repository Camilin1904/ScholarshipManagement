from django.forms import ModelForm
from .models import Scholarships


class CreateScholarshipForm(ModelForm):
    class Meta:
        model = Scholarships
        fields =  ['name', 'ID', 'description', 'donor', 'coverage', 'type', 'requirements']