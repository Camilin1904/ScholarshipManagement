from django.shortcuts import render
from django.shortcuts import redirect
from ..forms import *
from ..models import *
from django.http import HttpResponse


def createAppliStep3(request):


    if request.method == 'POST':
        try:

                error = ""

                print(request.POST)
                
                formPage2 = request.session.get('data_step_2', {})
                announcementPost = request.POST.get('announcement')
                postStudentCode = formPage2.get('studentCode')
                semesterPost = formPage2.get('semester') 
                statusPost = formPage2.get('status') 

                print(announcementPost)

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
            return render(
                request, 'home.html', 
                {'form': CreateAppliStep2Form, 'error': error})