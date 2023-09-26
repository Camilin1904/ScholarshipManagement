from django.shortcuts import render, redirect
from .forms import CreateApplicantForm
from .models import Applicant


def homeApplicant(request):
    return render(request, 'homeApplicant.html')

def applicants(request):
    applicants = Applicant.objects.all()
    return render(request, 'applicants.html', {'applicants': applicants})

def createApplicants(request):

    if request.method == 'GET':
        return render(request, 'createApplicant.html', {
            'form': CreateApplicantForm
        })
    else:
        try:
            form = CreateApplicantForm(request.POST)
            form.save()
            return redirect('/applicants/homePage/')
        except:
            return render(request, 'homeApplicant.html', {
                'form': CreateApplicantForm,
                'error': 'Please provide valid data'
            })
