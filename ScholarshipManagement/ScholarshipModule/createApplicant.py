from django.shortcuts import render
from django.shortcuts import redirect
from .forms import *
from .models import *
from django.http import HttpResponse

def createApplicants(request):

    if request.method == 'GET':
        return render(request, 'createApplicant.html', {
            'form': CreateApplicantForm,
            'error': ""
        })
    else:
        try:

            
            form = CreateApplicantForm(request.POST)
            error = ""
            postStudentCode = request.POST['studentCode']
            announcementPost = request.POST['announcement']
            postEmail = request.POST['email']
            statusPost = request.POST['status']
            semesterPost = request.POST['semester']

            try:
                verifyEmail= Applicant.objects.get(email = postEmail)
            except: 
                verifyEmail=1

            try:
                verifyStudentCode= Applicant.objects.get(studentCode = postStudentCode)
            except:
                verifyStudentCode=1
      

            try:
                
                
                if verifyStudentCode != 1:
                    error = 'El código de estudiante ya existe'    
                elif verifyEmail !=1:
                    error = 'El email de estudiante ya existe'
                else:
                    error = 'Digite información correctamente'
                form.save()

                if announcementPost == "":
                    error=""
                else: 
                    student = Applicant.objects.get(studentCode = postStudentCode)
                    announcement=Announcements.objects.get(id=announcementPost)

                    formNew = AnnouncementAndApplicantForm()
                    relation = formNew.save(commit=False)
                    relation.announcement = announcement
                    relation.applicant = student
                    relation.save()

                    formStatusCheck = StatusCheckAppliForm()
                    appliStatusCheck = formStatusCheck.save(commit=False)
                    appliStatusCheck.announcementCheck = announcement
                    appliStatusCheck.applicantCheck = student
                    appliStatusCheck.semester = semesterPost
                    appliStatusCheck.status = statusPost
                    appliStatusCheck.save()
                    
                    
                return redirect('/home/')
                

            except:
                print(error)
                return render(
                request, 'createApplicant.html', {'form': form, 'error': error})

        except:
            return render(request, 'home.html', {
                'form': CreateApplicantForm,
                'error': error
            })