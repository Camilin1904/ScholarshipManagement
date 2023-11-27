from django.shortcuts import render
from django.shortcuts import redirect
from ..forms import *
from ..models import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .isAllowed import isAllowed


@login_required(login_url="/login")
def createAppliStep3(request):

    if not (isAllowed(request.user, 1)):
        return redirect("/home")

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

                    try: 
                        announAppli = AnnouncementAndApplicant.objects.get(applicant = student)
                        announcement=Announcements.objects.get(id=announcementPost)

                        announAppli.deleted = False
                        announAppli.announcement = announcement
                        announAppli.applicant = student
                        announAppli.save()

                        formStatusCheck = StatusCheckAppliForm()
                        appliStatusCheck = formStatusCheck.save(commit=False)
                        appliStatusCheck.announcementCheck = announcement
                        appliStatusCheck.applicantCheck = student
                        appliStatusCheck.semester = student.semester
                        appliStatusCheck.status = 0
                        appliStatusCheck.save()



                        Applicant.objects.filter(studentCode=postStudentCode).update(status=0)

                        return redirect('/home/')   
                    except:
                        announAppli = None

                    if announAppli == None:
                        
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
                        appliStatusCheck.semester = student.semester
                        appliStatusCheck.status = 0
                        appliStatusCheck.save()



                        Applicant.objects.filter(studentCode=postStudentCode).update(status=0)

                return redirect('/home/')


        except:
            return render(
                request, 'home.html', 
                {'form': CreateAppliStep2Form, 'error': error})
