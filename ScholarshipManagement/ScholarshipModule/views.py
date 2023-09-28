from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import CreateScholarshipForm, CreateAnnouncementForm, CreateAnnouncementEventForm, CreateScholarshipAnnouncementForm
from .models import Scholarships, Announcements

# Create your views here.


def signUp(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # Register user :)
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Username already exists'
                })

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'The passwords do not match'
        })


def home(request):
    return render(request, 'home.html')


def scholarships(request):
    scholarships = Scholarships.objects.all()
    return render(request, 'scholarships.html', {'scholarships': scholarships})


def createScholarships(request):

    if request.method == 'GET':
        return render(request, 'createScholarship.html', {
            'form': CreateScholarshipForm
        })
    else:
        try:
            form = CreateScholarshipForm(request.POST)
            form.save()
            return redirect('scholarships')
        except:
            return render(request, 'createScholarship.html', {
                'form': CreateScholarshipForm,
                'error': 'Please provide valid data'
            })


def signout(request):
    logout(request)
    return redirect('home')


def signin(request):

    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user == None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('tasks')
        
        
def createAnnouncement(request):

    if request.method == 'GET':
        return render(request, 'createAnnouncement.html', {
            'announcementForm': CreateAnnouncementForm (prefix="announcementForm"),
            'scholarshipAnnouncementForm': CreateScholarshipAnnouncementForm (prefix="scholarshipAnnouncementForm"),
            'announcementEventFormInscription': CreateAnnouncementEventForm (prefix="announcementEventFormInscription"),
            'announcementEventFormSelection': CreateAnnouncementEventForm (prefix="announcementEventFormSelection"),
            'announcementEventFormInterview': CreateAnnouncementEventForm (prefix="announcementEventFormInterview"),
            'announcementEventFormPublication': CreateAnnouncementEventForm (prefix="announcementEventFormPublication")
        })
    else:



        announcementForm = CreateAnnouncementForm(request.POST,prefix="announcementForm")
        scholarshipAnnouncementForm = CreateScholarshipAnnouncementForm(request.POST,prefix="scholarshipAnnouncementForm")

        announcementForm.save()

        announcementFormObj= Announcements.objects.latest('id')

        scholarshipAnnouncementFormInstance = scholarshipAnnouncementForm.save(commit=False)
        scholarshipAnnouncementFormInstance.announcementId=announcementFormObj
        scholarshipAnnouncementFormInstance.save()

        events=["announcementEventFormInscription","announcementEventFormSelection","announcementEventFormInterview","announcementEventFormPublication"]
        eventNum=0

        for event in events:

            announcementEventForm=CreateAnnouncementEventForm(request.POST,prefix=event)
            announcementEventFormInstance = announcementEventForm.save(commit=False)
            announcementEventFormInstance.announcementId=announcementFormObj
            announcementEventFormInstance.type=eventNum
            announcementEventFormInstance.save()

            eventNum+=1

        return redirect('home')
        

        """
        
        try:
 
        
        except:

            return render(request, 'createAnnouncement.html', {
            'form1': CreateAnnouncementForm (prefix="form1"),
            'form2': CreateScholarshipAnnouncementForm (prefix="form2"),
            'form3': CreateAnnouncementEventForm (prefix="form3"),
            'form4': CreateAnnouncementEventForm (prefix="form4"),
            'form5': CreateAnnouncementEventForm (prefix="form5"),
            'form6': CreateAnnouncementEventForm (prefix="form6"),
            'error': 'Please provide valid data'

            
            })
            """
