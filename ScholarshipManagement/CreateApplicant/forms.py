from django.forms import ModelForm
from .models import Applicant


class CreateApplicantForm(ModelForm):
    class Meta:
        model = Applicant
        fields = ['name', 'lastName', 'studentCode',
                  'faculty', 'major', 'semester','email', 'phone']