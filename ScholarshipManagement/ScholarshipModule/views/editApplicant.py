from django.shortcuts import render
from django.shortcuts import redirect
from ..forms import *
from ..models import *
from django.http import HttpResponse
from datetime import date
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login")
def editApplicant(request):

    studentCodeSt = request.session.get('studentCode')
    applicant = Applicant.objects.filter(studentCode = studentCodeSt)
    
    idSt = applicant.first().ID
    
    
    if request.method == 'GET':
        announcement=None
       
        name = applicant.first().name
        lastName = applicant.first().lastName
        faculty = applicant.first().faculty
        major = applicant.first().major
        semester = applicant.first().semester
        email = applicant.first().email
        phone = applicant.first().phone
        status = applicant.first().status
        image = applicant.first().image

        if image == "":
            image = "none"
        

        try:
            announcement = AnnouncementAndApplicant.objects.filter(applicant=idSt).first().announcement
            announNoDeleted = AnnouncementAndApplicant.objects.get(applicant=idSt)
            if announNoDeleted.deleted == True:
                announcement = None
        except:
            announcement = None    
  

        form = CreateApplicantForm(initial={'name': name,
                                            'lastName': lastName,
                                            'studentCode': studentCodeSt,
                                            'faculty':faculty,
                                            'major': major,
                                            'semester': semester,
                                            'email': email,
                                            'phone':phone,
                                            'status':status,
                                            'announcement':announcement})
        
        return render(request,'./HTML/editApplicant.html',{'form':form, 'image': image, 'Applicant': applicant})
    
    else:
        applicant = Applicant.objects.get(studentCode = studentCodeSt)
        applicant2 = Applicant.objects.get(studentCode = studentCodeSt)

        if 'delete' in request.POST:
            
            try:
                announcement = AnnouncementAndApplicant.objects.get(applicant=idSt)
                if announcement.deleted == False:
                    announcement.deleted = True
                    announcement.save()

                    applicant.status = 2
                    applicant.save()

                    formStatusCheck = StatusCheckAppliForm()
                    appliStatusCheck = formStatusCheck.save(commit=False)
                    appliStatusCheck.announcementCheck = announcement.announcement
                    appliStatusCheck.applicantCheck = applicant
                    appliStatusCheck.semester = applicant.semester
                    appliStatusCheck.status = 2
                    appliStatusCheck.save()
            
                    return redirect('/view/Student')
            except:
                announcement = None  

                

        
        if 'changeAnnoun' in request.POST:

            request.session['data_step_1'] = request.POST
            
            error = ""
            announcements = AnnouncementEvent.objects.filter(type = "Inscription").filter(startingDate__lte = date.today()).filter(endDate__gte = date.today())
            announcements = announcements.values_list('announcementId', flat=True)
            scholarshipAnnouns=ScholarshipAnnouncements.objects.filter(announcementId__in = announcements)

            return render(
                request, './HTML/createAppliStep3.html', 
                {'error': error, 'scholarshipAnnoun': scholarshipAnnouns})

            
        
        Applicant.objects.filter(studentCode=studentCodeSt).update(name=request.POST['name'],
                                                                   lastName=request.POST['lastName'],
                                                                   faculty=request.POST['faculty'],
                                                                   major=request.POST['major'],
                                                                   semester=request.POST['semester'],
                                                                   email=request.POST['email'],
                                                                   phone=request.POST['phone'],
                                                                   status=request.POST['status'])
        
        
        try:
            if request.POST['announcement'] != "":
                announcementGet = Announcements.objects.get(id = request.POST['announcement'])
        except:
            return redirect('/view/Student')
        
        applicant.name = request.POST['name']
        applicant.lastName = request.POST['lastName']
        applicant.studentCode = applicant2.studentCode
        applicant.faculty = request.POST['faculty']
        applicant.major = request.POST['major']
        applicant.semester = request.POST['semester']
        applicant.email = request.POST['email']
        applicant.phone = request.POST['phone']
        applicant.status=request.POST['status']

       

        applicant.save()

        
        form = CreateApplicantForm(request.POST, request.FILES, instance=applicant) 
        form.save()


    
        if request.POST['announcement'] == "":
            announcementChange = None
                
        else:
         
            try:
                announcementChange = AnnouncementAndApplicant.objects.get(applicant=idSt)
                
                #Change the applicant previous announcement to a new one here its the register of the elimination 
                if announcementChange.delete == False:
                    
                    applicant.status = 2
                    applicant.save()

                    formStatusCheck = StatusCheckAppliForm()
                    appliStatusCheck = formStatusCheck.save(commit=False)
                    appliStatusCheck.announcementCheck = announcementChange.announcement
                    appliStatusCheck.applicantCheck = applicant
                    appliStatusCheck.semester = applicant.semester
                    appliStatusCheck.status = applicant.status
                    appliStatusCheck.save()

                announcementChange.announcement = announcementGet
                announcementChange.deleted = False
                announcementChange.save()
                
                #Register of the new announcement

                #Check if the user change the status
                if applicant2.status == int(request.POST['status']):
                    applicant.status = 0
                    applicant.save()
                else:
                    applicant.status = request.POST['status']
                    applicant.save()


                formStatusCheck = StatusCheckAppliForm()
                appliStatusCheck = formStatusCheck.save(commit=False)
                appliStatusCheck.announcementCheck = announcementGet
                appliStatusCheck.applicantCheck = applicant
                appliStatusCheck.semester = applicant.semester
                appliStatusCheck.status = applicant.status
                appliStatusCheck.save()

            except:
                formNew= AnnouncementAndApplicantForm()
                relation=formNew.save(commit=False)
                relation.announcement=announcementGet
                relation.applicant=applicant
                relation.save()

                #Check if the user change the status
                if applicant2.status == int(request.POST['status']):
                    applicant.status = 0
                    applicant.save()
                else:
                    applicant.status = request.POST['status']
                    applicant.save()

                formStatusCheck = StatusCheckAppliForm()
                appliStatusCheck = formStatusCheck.save(commit=False)
                appliStatusCheck.announcementCheck = announcementGet
                appliStatusCheck.applicantCheck = applicant
                appliStatusCheck.semester = applicant.semester
                appliStatusCheck.status = applicant.status
                appliStatusCheck.save()


        try:
            del request.session['name']
        except:
            print(0)

        return redirect('/view/Student')