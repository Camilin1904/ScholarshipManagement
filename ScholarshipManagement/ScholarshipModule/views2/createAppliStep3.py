from django.shortcuts import render
from django.shortcuts import redirect
from ..forms import *
from ..models import *
from django.http import HttpResponse


def createAppliStep3(request):


    if request.method == 'POST':
        try:


                if 'skip' in request.POST:
                     return redirect('/home/')
                     
                error = ""


                formPage2 = request.session.get('data_step_1', {})
                announcementPost = request.POST.get('announcement')
                postStudentCode = formPage2.get('studentCode')


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

                    Applicant.objects.filter(studentCode=postStudentCode).update(status=0)
                    
                    
                return redirect('/home/')


        except:
            return render(
                request, 'home.html', 
                {'form': CreateAppliStep2Form, 'error': error})