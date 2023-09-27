from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import CreateScholarshipForm, CreateAnnouncementForm, CreateAnnouncementEventForm, CreateScholarshipAnnouncementForm
from .models import Scholarships

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
            'form1': CreateAnnouncementForm (prefix="form1"),
            'form2': CreateScholarshipAnnouncementForm (prefix="form2"),
            'form3': CreateAnnouncementEventForm (prefix="form3"),
            'form4': CreateAnnouncementEventForm (prefix="form4"),
            'form5': CreateAnnouncementEventForm (prefix="form5"),
            'form6': CreateAnnouncementEventForm (prefix="form6")
        })
    else:
        """

        form1 = CreateAnnouncementForm(request.POST,prefix="form1")
        form2 = CreateScholarshipAnnouncementForm(request.POST,prefix="form2")

        form3 = CreateAnnouncementEventForm(request.POST,prefix="form3")
        form4 = CreateAnnouncementEventForm(request.POST,prefix="form4")
        form5 = CreateAnnouncementEventForm(request.POST,prefix="form5")
        form6 = CreateAnnouncementEventForm(request.POST,prefix="form6")

        
        form1Objt=form1.save()


        announcementId= form1Objt.id

        form2.initial['announcementId'] = announcementId

        form3.initial['AnnouncementId'] = announcementId
        form3.initial['EventType'] = announcementId

        form4.initial['AnnouncementId'] = announcementId
        form4.initial['EventType'] = announcementId
        
        form5.initial['AnnouncementId'] = announcementId
        form5.initial['EventType'] = announcementId

        form6.initial['AnnouncementId'] = announcementId
        form6.initial['EventType'] = announcementId

        
        form2.save()
        form3.save()
        form4.save()
        form5.save()
        form6.save()

        """
        
        try:
            """


            form1 = CreateAnnouncementForm(request.POST,prefix="form1")
            form2 = CreateScholarshipAnnouncementForm(request.POST,prefix="form2")

            form3 = CreateAnnouncementEventForm(request.POST,prefix="form3")
            form4 = CreateAnnouncementEventForm(request.POST,prefix="form4")
            form5 = CreateAnnouncementEventForm(request.POST,prefix="form5")
            form6 = CreateAnnouncementEventForm(request.POST,prefix="form6")

            
            form1Objt=form1.save()

            announcementId= form1Objt.id

            
            
            form2['announcementId']=announcementId

            form3['AnnouncementId']=announcementId
            form3['EventType']= 0

            form4['AnnouncementId']=announcementId
            form4['EventType']= 1

            form5['AnnouncementId']=announcementId
            form5['EventType']= 2

            form6['AnnouncementId']=announcementId
            form6['EventType']= 3

            
            form2.save()
            form3.save()
            form4.save()
            form5.save()
            form6.save()

            

            """

            return redirect('home')
        
        
        except:

            """
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
