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
import io
import csv


# Create your views here.

def signUp(request):

    if request.method == 'POST':
        # Save the form answers
        form = CreateNewUser(request.POST)
        error = ''
        for field in form:
            # Errors as text
            error = error + (field.errors)
            
        if form.is_valid():
            # Save user in data base
            user = form.save()
            # Django login method
            login(request, user)
            return redirect('/home')
        else:
            print("Me cago en todo lo cagable")
            print(error)
            return render(
                request, './HTML/signup.html', {'form': form, 'error': error})
    else:
        form = CreateNewUser
    return render(
        request, './HTML/signup.html', {'form': form, 'error':''})

def signOut(request):
    
    logout(request)
    return redirect('/')

def signIn(request):

    error = ''

    if request.method == "POST":
        # For some reason django failes if I save the form in a variable
        # so i saved each answer
        username = request.POST['username']
        password = request.POST['password']
        try:
            # If the user is not found it creates an exception
            user = User.objects.get(username=username)
            # If the username and password match or not the data base will return
            # None or a User object
            user = authenticate(
                request, username=username, password=password)
            if user is not None:
                # If the fields match with the data base then login the user
                login(request, user)
                # Redirect home
                return redirect('/home')
            else:
                # If the data base returns None
                error = 'El usuario o la contraseña son erroneos'
        except:
            # If the username is not found
            error = 'El usuario no existe'

    return render(
        request, './HTML/login.html', {
            'form': Login,
            'error': error
        })


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

         
        
def searchUserForRole(request):
    user = request.user
    success = ""
    if request.method == 'POST':
        try:
            username = request.POST['username']
            toChange = User.objects.get(id=username)
            try:
                # If the user is not found it creates an exception
                return render(
                    request, './HTML/roleAssign.html', {
                        'form': roleAssign,
                        'toChange' : toChange
                    })
            except:
                # If the username field does not exists
                success = 'El usuario no existe'
        except:
            #username field does not exist so we are in roleAssign
            rol = request.POST['role']
            email = request.POST['email']
            toChange = User.objects.filter(username=email).update(role=rol)
            success = 'El cambio de rol ha sido exitoso'


    else:
        if user.role == 0:
            return render(
                request, './HTML/searchUser.html', {
                    'form': searchUser,
                    'success': success
                })
        else:
            return redirect('/home')
         
    return render(
        request, './HTML/searchUser.html', {
            'form': searchUser,
            'success': success
        })

            
def searchStudent(request):
    return render(
            request, './HTML/searchStudent.html')
