from django.shortcuts import render
from django.shortcuts import redirect
from ..forms import *
from ..models import *
from django.http import HttpResponse


def createApplicants(request):


    if request.method == 'GET':
        return render(request, 'createApplicant.html', {
            'form': CreateAppliStep1Form,
            'error': ""
        })
    else:
        try:
            form = CreateAppliStep1Form(request.POST)
            error = ""
            postEmail = request.POST['email']
            

            try:
                Applicant.objects.get(email = postEmail)

                error = 'El email de estudiante ya existe'
                return render(
                    request, 'createApplicant.html', 
                    {'form': form,'error': error})
            except: 
                request.session['data_step_1'] = request.POST

                return render(
                    request, 'createAppliStep2.html', 
                    {'form': CreateAppliStep2Form, 'error': error})
                
        except:
            return render(
                request, 'home.html', 
                {'form': form, 'error': error
            })