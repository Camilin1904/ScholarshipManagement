from django.shortcuts import render
from django.shortcuts import redirect
from ..forms import *
from ..models import *
from django.http import HttpResponse
from datetime import date


def createApplicants(request):


    if request.method == 'GET':
        return render(request, 'createApplicant.html', {
            'form': CreateAppliStep1Form,
            'form2': CreateAppliStep2Form,
            'error': ""
        })
    else:
        try:
            form = CreateApplicantForm(request.POST, request.FILES)

            formError1 = CreateAppliStep1Form(request.POST, request.FILES)
            formError2 = CreateAppliStep2Form(request.POST)
            
            
            error = ""
            postEmail = request.POST['email']
            postStudentCode = request.POST['studentCode']

    
            try:
                Applicant.objects.get(email = postEmail)

                error = 'El email de estudiante ya existe'
                return render(request, 'createApplicant.html', {
                    'form': formError1,'form2': formError2,'error': error})
            
            except: 
                try:
                    Applicant.objects.get(studentCode = postStudentCode)

                    error = "El código de estudiante ya existe"
                    return render(request, 'createApplicant.html', {
                        'form': CreateAppliStep1Form,'form2': CreateAppliStep2Form,'error': error})
                
                except:
                    form.save()
                    request.session['data_step_1'] = request.POST
                    
                    
                    announcements = AnnouncementEvent.objects.filter(type = "Inscription").filter(startingDate__lte = date.today()).filter(endDate__gte = date.today())
                    announcements = announcements.values_list('announcementId', flat=True)
                    scholarshipAnnouns=ScholarshipAnnouncements.objects.filter(announcementId__in = announcements)

                    return render(
                        request, 'createAppliStep3.html', 
                        {'error': error, 'scholarshipAnnoun': scholarshipAnnouns})
                
        except:
            return render(
                request, 'home.html', 
                {'form': form, 'error': error
            })