from django.shortcuts import render
from django.shortcuts import redirect
from ..forms import *
from ..models import *
from django.http import HttpResponse


def createAppliStep2(request):


    if request.method == 'POST':
        try:

            if 'back' in request.POST: 
                return render(
                    request, 'createApplicant.html', 
                    {'form': formpage1Back,'error': error}) 
            
            formPage1 = request.session.get('data_step_1', {})
            formpage1Back = CreateAppliStep1Form(formPage1)
            formPage2 = CreateAppliStep2Form(request.POST)
            error = ""
            postStudentCode = request.POST['studentCode']
            statusPost = request.POST['status']
            semesterPost = request.POST['semester']
            facultyPost = request.POST['faculty']
            majorPost = request.POST['major']



            try:
                Applicant.objects.get(studentCode = postStudentCode)
                error = "El código de estudiante ya existe"
                return render(
                    request, 'createAppliStep2.html', 
                    {'form': formPage2,'error': error})
            except:
                    error = ""
                    form = CreateApplicantForm()
                    appliCreation = form.save(commit=False)
                    appliCreation.name = formPage1.get('name')
                    appliCreation.lastName = formPage1.get('lastName')
                    appliCreation.email = formPage1.get('email')
                    appliCreation.phone = formPage1.get('phone','')
                    appliCreation.image = formPage1.get('image','')
                    appliCreation.studentCode = postStudentCode
                    appliCreation.status = statusPost
                    appliCreation.semester = semesterPost
                    appliCreation.faculty = facultyPost
                    appliCreation.major = majorPost
                    appliCreation.save()

                    scholarshipAnnouns=ScholarshipAnnouncements.objects.all()
                    request.session['data_step_2'] = request.POST

                    return render(
                        request, 'createAppliStep3.html', 
                        {'error': error, 'scholarshipAnnoun': scholarshipAnnouns})
            

        except:
            return render(
                request, 'home.html', 
                {'form': CreateAppliStep2Form, 'error': error})