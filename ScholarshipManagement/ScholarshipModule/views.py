from random import random
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.http import HttpResponse

# Create your views here.


def signUp(request):

    if request.method == 'POST':
        # Save the form answers
        form = CreateNewUser(request.POST)
        error = ''
        for field in form:
            # Errors as text
            error = field.errors.as_text
        if form.is_valid():
            # Save user in data base
            user = form.save()
            # Django login method
            login(request, user)
            return redirect('/home')
        else:
            return render(
                request, './HTML/Signin.html', {'form': form, 'error': error})
    else:
        form = CreateNewUser
    return render(
        request, './HTML/Signin.html', {'form': form, 'error':''})

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

# The tag will demand the user to login
@login_required(login_url="/login")
def home(request):
    user = request.user
    if user.role == 0:
        return render(request, './HTML/homeAdmin.html')
    elif user.role == 1:
        return render(request, './HTML/homeFinancial.html')
    elif user.role == 2:
        return render(request, './HTML/homePhilanthropy.html')
    else:
        return render(request, './HTML/notAcces.html')


def scholarships(request):
    
    scholarships = Scholarships.objects.all()
    return render(
        request, 'scholarships.html', {
            'scholarships': scholarships
        })


def createScholarships(request):

    if request.method == 'GET':
        return render(
            request, 'createScholarship.html', {
                'form': CreateScholarshipForm
            })
    else:
        try:
            form = CreateScholarshipForm(request.POST)
            form.save()
            return redirect('scholarships')
        except:
            return render(
                request, 'createScholarship.html', {
                'form': CreateScholarshipForm,
                'error': 'Please provide valid data'
            })
        
def searchApplicant(request):
    
    applicant = None
    
    if request.method == 'GET':
         
        nameSearch = request.GET.get('name')

        if nameSearch == None:
            applicant = Applicant.objects.all();
        else:
            applicant = Applicant.objects.filter(name=nameSearch)

        return render(request,'./HTML/searchApplicant.html',{'applicant':applicant}) 
    else:
        try:
            del request.session['name']
        except:
            print(0)
       
        request.session['name'] = request.POST
        studentCodeSt = request.session.get('name')
        applicant = Applicant.objects.filter(name = studentCodeSt)

           
        return render(request,'./HTML/applicant.html',{'applicant':applicant,
                                                       'studentCodeSt':studentCodeSt})
    
        
    


def createApplicants(request):

    if request.method == 'GET':
        return render(request, 'createApplicant.html', {
            'form': CreateApplicantForm
        })
    else:
        try:

            AnnouncementPost = 0
            form = CreateApplicantForm(request.POST)
            error = ""
            postStudentCode = request.POST['studentCode']
            AnnouncementPost = request.POST['announcement']
            postEmail = request.POST['email']

            try:
                verifyEmail= Applicant.objects.get(email = postEmail)
            except: 
                verifyEmail=1;

            try:
                verifyStudentCode= Applicant.objects.get(studentCode = postStudentCode)
            except:
                verifyStudentCode=1;
      

            try:
                
                
                if verifyStudentCode != 1:
                    error = 'El código de estudiante ya existe'    
                elif verifyEmail !=1:
                    error = 'El email de estudiante ya existe'
                else:
                    error = 'Digite información correctamente'
                form.save()

                if AnnouncementPost == "":
                    error=""
                else: 
                    student = Applicant.objects.get(studentCode = postStudentCode)
                    annuncement=Announcement.objects.get(ID=AnnouncementPost)

                    print(student.ID,AnnouncementPost)

                    formNew= AnnouncementAndApplicantForm()
                    relation=formNew.save(commit=False)
                    relation.announcement=annuncement
                    relation.applicantID=student
                    relation.save()
                    
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
        
        
def searchUserForRole(request):
    user = request.user
    error = ""
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
                # If the username is not found
                error = 'El usuario no existe'
        except:
            #username field does not exist so we are in roleAssign
            rol = request.POST['role']
            email = request.POST['email']
            toChange = User.objects.filter(username=email).update(role=rol)
            print("se supone que hubo cambios")
            redirect(home)


    else:
        if user.role == 0:
            return render(
                request, './HTML/searchUser.html', {
                    'form': searchUser
                })
        else:
            return redirect('/home')
    return render(
        request, './HTML/searchUser.html', {
            'form': searchUser,
            'error': error
        })
