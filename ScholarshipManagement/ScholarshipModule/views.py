from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import CreateScholarshipForm, CreateAnnouncementForm, CreateAnnouncementEventForm, CreateScholarshipAnnouncementForm, CreateAnnouncementAdditionalEventForm
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

    additionalEvents=0
    datalist=[]

    context= {
            'announcementForm': CreateAnnouncementForm (prefix="announcementForm"),
            'scholarshipAnnouncementForm': CreateScholarshipAnnouncementForm (prefix="scholarshipAnnouncementForm"),
            'announcementEventFormInscription': CreateAnnouncementEventForm (prefix="announcementEventFormInscription"),
            'announcementEventFormSelection': CreateAnnouncementEventForm (prefix="announcementEventFormSelection"),
            'announcementEventFormInterview': CreateAnnouncementEventForm (prefix="announcementEventFormInterview"),
            'announcementEventFormPublication': CreateAnnouncementEventForm (prefix="announcementEventFormPublication"),

            "data" : datalist,

            'additionalEvents':additionalEvents
            
        }

    if request.method == 'GET':
        return render(request, 'createAnnouncement.html', context)
    
    else:

        if 'saveBttn' in request.POST:

            announcementForm = CreateAnnouncementForm(request.POST,prefix="announcementForm")
            scholarshipAnnouncementForm = CreateScholarshipAnnouncementForm(request.POST,prefix="scholarshipAnnouncementForm")

            announcementForm.save()

            announcementFormObj= Announcements.objects.latest('id')

            scholarshipAnnouncementFormInstance = scholarshipAnnouncementForm.save(commit=False)
            scholarshipAnnouncementFormInstance.announcementId=announcementFormObj
            scholarshipAnnouncementFormInstance.save()

            events=["announcementEventFormInscription","announcementEventFormSelection","announcementEventFormInterview","announcementEventFormPublication"]
            eventNum=0

            eventType=["Inscription","Selection","Interview","Publication"]

            for event in events:

                announcementEventForm=CreateAnnouncementEventForm(request.POST,prefix=event)
                announcementEventFormInstance = announcementEventForm.save(commit=False)
                announcementEventFormInstance.announcementId=announcementFormObj
                announcementEventFormInstance.type=eventType[eventNum]
                announcementEventFormInstance.save()

                eventNum+=1

            additionalEvents= int(request.POST['title']) +1

            if(additionalEvents!=0):

                for x in range (additionalEvents-1):

                    announcementAdditionalEventForm=CreateAnnouncementAdditionalEventForm(request.POST,prefix="announcementAdditionalEventForm"+ str(x))
                    announcementAdditionalEventFormInstance = announcementAdditionalEventForm.save(commit=False)
                    announcementAdditionalEventFormInstance.announcementId=announcementFormObj
                    announcementAdditionalEventFormInstance.save()
 

            return redirect('home')
        
        if 'newEventBttn' in request.POST:

            additionalEvents= int(request.POST['title']) +1

            if (additionalEvents!=1):

                for x in range (additionalEvents-1):

                    datalist.append(CreateAnnouncementAdditionalEventForm ( request.POST, prefix="announcementAdditionalEventForm"+ str(x)))

                    context["announcementAdditionalEventForm"+ str(x)] = datalist[x]
                    
            datalist.append(CreateAnnouncementAdditionalEventForm ( prefix="announcementAdditionalEventForm"+ str(additionalEvents-1)))
            context["announcementAdditionalEventForm"+ str(additionalEvents)]=datalist[additionalEvents-1]


            context= {
            'announcementForm': CreateAnnouncementForm (request.POST, prefix="announcementForm"),
            'scholarshipAnnouncementForm': CreateScholarshipAnnouncementForm (request.POST, prefix="scholarshipAnnouncementForm"),
            'announcementEventFormInscription': CreateAnnouncementEventForm (request.POST, prefix="announcementEventFormInscription"),
            'announcementEventFormSelection': CreateAnnouncementEventForm (request.POST, prefix="announcementEventFormSelection"),
            'announcementEventFormInterview': CreateAnnouncementEventForm (request.POST, prefix="announcementEventFormInterview"),
            'announcementEventFormPublication': CreateAnnouncementEventForm (request.POST, prefix="announcementEventFormPublication"),
            "data" : datalist,
            'additionalEvents':additionalEvents,
            }

            return render(request, 'createAnnouncement.html', context)
        
        if 'deleteEventBttn' in request.POST:

            additionalEvents= int(request.POST['title']) -1

            print(additionalEvents)

            for x in range (additionalEvents):

                datalist.append(CreateAnnouncementAdditionalEventForm ( request.POST, prefix="announcementAdditionalEventForm"+ str(x)))

                context["announcementAdditionalEventForm"+ str(x)] = datalist[x]


            context= {
            'announcementForm': CreateAnnouncementForm (request.POST, prefix="announcementForm"),
            'scholarshipAnnouncementForm': CreateScholarshipAnnouncementForm (request.POST, prefix="scholarshipAnnouncementForm"),
            'announcementEventFormInscription': CreateAnnouncementEventForm (request.POST, prefix="announcementEventFormInscription"),
            'announcementEventFormSelection': CreateAnnouncementEventForm (request.POST, prefix="announcementEventFormSelection"),
            'announcementEventFormInterview': CreateAnnouncementEventForm (request.POST, prefix="announcementEventFormInterview"),
            'announcementEventFormPublication': CreateAnnouncementEventForm (request.POST, prefix="announcementEventFormPublication"),
            "data" : datalist,

            'additionalEvents':additionalEvents,
            }

            return render(request, 'createAnnouncement.html', context)
            
            
            
        

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
