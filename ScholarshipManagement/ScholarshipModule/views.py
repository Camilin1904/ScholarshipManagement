from django.contrib.auth.models import User
from datetime import date
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

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

        if 'delete' in request.POST:
            
            try:
                announcement = AnnouncementAndApplicant.objects.get(applicant=idSt)
                announcement.deleted = True
                announcement.save()
            except:
                announcement = None  

            return redirect('/view/Student')

        Applicant.objects.filter(studentCode=studentCodeSt).update(name=request.POST['name'],
                                                                   lastName=request.POST['lastName'],
                                                                   faculty=request.POST['faculty'],
                                                                   major=request.POST['major'],
                                                                   semester=request.POST['semester'],
                                                                   email=request.POST['email'],
                                                                   phone=request.POST['phone'],
                                                                   status=request.POST['status'])
        
        
        try:
            announcementGet = Announcements.objects.get(id = request.POST['announcement'])
        except:
            return redirect('/view/Student')
        
        student = Applicant.objects.get(studentCode = studentCodeSt)
        form = CreateApplicantForm(request.POST, request.FILES, instance=student) 
        form.save()
        
        if request.POST['announcement'] == "":

            try:
                announcementChange = AnnouncementAndApplicant.objects.get(applicant=idSt)
                announcementChange.announcement = None
                announcementChange.deleted = False
                announcementChange.save()


            except:
                announcementChange = None
                
        else:
            try:
                announcementChange = AnnouncementAndApplicant.objects.get(applicant=idSt)
                announcementChange.announcement = announcementGet
                announcementChange.deleted = False
                announcementChange.save()


            except:
                formNew= AnnouncementAndApplicantForm()
                relation=formNew.save(commit=False)
                relation.announcement=announcementGet
                relation.applicant=applicant
                relation.save()



        try:
            del request.session['name']
        except:
            print(0)

        return redirect('/view/Student')
    
def viewApplicant(request):
    studentCodeSt = request.session.get('studentCode')
    applicant = Applicant.objects.filter(studentCode = studentCodeSt)
    idSt = applicant.first().ID

    try:
        announcement = AnnouncementAndApplicant.objects.filter(applicant=idSt).first().announcement.id
        announNoDeleted = AnnouncementAndApplicant.objects.get(applicant=idSt)
        if announNoDeleted.deleted == True:
            announcement = None
    except:
        announcement = None

    if request.method == 'GET':
        return render(request,'./HTML/viewApplicant.html',{'applicant':applicant,
                                                           'announcement':announcement, 'error': ''})
    else:
        if 'back' in request.POST:
            return redirect("/searchStudent/")
        elif 'edit' in request.POST:
       
            print(request.POST)
            request.session['studentCode'] = request.POST['edit']

            return redirect('/applicants/edit')
        elif 'delete' in request.POST:
            applicantDelete = Applicant.objects.get(studentCode = studentCodeSt)
            applicantDelete.deleted = True
            if announcement == None:
                applicantDelete.save()
            else:
                announNoDeleted.deleted = True
                announNoDeleted.save()
                applicantDelete.save()

           

            return redirect("/searchStudent/")

            
def searchStudent(request):
    return render(
            request, './HTML/searchStudent.html')
