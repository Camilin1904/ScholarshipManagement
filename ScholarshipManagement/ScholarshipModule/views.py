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
from itertools import chain

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
    return render(request, './HTML/scholarships.html', 
                  {'./HTML/scholarships': scholarships})


def createScholarships(request):

    if request.method == 'GET':
        return render(request, './HTML/createScholarship.html', {
            'form': CreateScholarshipForm
        })
    else:
        try:
            form = CreateScholarshipForm(request.POST)
            form.save()
            return redirect('scholarships')
        except:
            return render(request, './HTML/createScholarship.html', {
                'form': CreateScholarshipForm,
                'error': 'Please provide valid data'
            })
        


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
                    annuncement=Announcements.objects.get(id=AnnouncementPost)

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
            
def createAnnouncement(request):

    additionalEvents = 0
    datalist = []
    context = {
            'announcementForm': CreateAnnouncementForm (prefix="announcementForm"),
            'scholarshipAnnouncementForm': CreateScholarshipAnnouncementForm (prefix="scholarshipAnnouncementForm"),
            'announcementEventFormInscription': CreateAnnouncementEventForm (prefix="announcementEventFormInscription"),
            'announcementEventFormSelection': CreateAnnouncementEventForm (prefix="announcementEventFormSelection"),
            'announcementEventFormInterview': CreateAnnouncementEventForm (prefix="announcementEventFormInterview"),
            'announcementEventFormPublication': CreateAnnouncementEventForm (prefix="announcementEventFormPublication"),
            "data" : datalist,
            'additionalEvents': additionalEvents,
            'error':""
        }

    if request.method == 'GET':

        return render(
            request, 'createAnnouncement.html', context)
    
    else:

        try:

            if 'saveBttn' in request.POST:

                eventType = [
                    'Inscription','Interview','Selection','Publication']
                today = str(date.today())
                additionalEvents = int(request.POST['title']) + 1
                scholarshipIdInt = int(request.POST['scholarshipAnnouncementForm-scholarshipId'])

                if (not Scholarships.objects.filter(ID =scholarshipIdInt).exists()):

                    raise Exception("La beca seleccionada no está registrada")

                count = 3 + additionalEvents

                for x in range (count):

                    if(x <= 3):

                        initString = 'announcementEventForm' +  eventType[x] + '-startingDate'
                        endString = 'announcementEventForm' + eventType[x] + '-endDate'

                    else:

                        initString = 'announcementAdditionalEventForm' +  str(x - 4) + '-startingDate'
                        endString = 'announcementAdditionalEventForm' + str(x - 4) + '-endDate'
                        additionalType = 'announcementAdditionalEventForm'+ str(x - 4) + '-type'
                        additionalTypeStr = request.POST[additionalType]

                        if(not bool(additionalTypeStr)):

                            raise Exception("Se deben llenar los campos de tipo de convocatoria")

                    initialDate = request.POST[initString]
                    endDate = request.POST[endString]
                    
                    if ( not bool(initialDate) or not bool(endDate)):

                        raise Exception("Se deben llenar todos los campos de fecha")

                    if (today > initialDate or today > endDate):

                        raise Exception("Se deben seleccionar fechas posteriores al día de hoy")

                    if (initialDate >= endDate):
                        raise Exception("La fecha final debe ser posterior a la fecha incial")
                
                announcementForm = CreateAnnouncementForm(request.POST,prefix="announcementForm")
                scholarshipAnnouncementForm = CreateScholarshipAnnouncementForm(request.POST,prefix="scholarshipAnnouncementForm")
                announcementForm.save()

                announcementFormObj = Announcements.objects.latest('id')

                scholarshipAnnouncementFormInstance = scholarshipAnnouncementForm.save(commit=False)
                scholarshipAnnouncementFormInstance.announcementId = announcementFormObj
                scholarshipAnnouncementFormInstance.save()

                events = [
                    "announcementEventFormInscription","announcementEventFormInterview",
                    "announcementEventFormSelection","announcementEventFormPublication"]
                eventNum = 0

                for event in events:

                    announcementEventForm = CreateAnnouncementEventForm(request.POST,prefix=event)
                    announcementEventFormInstance = announcementEventForm.save(commit=False)
                    announcementEventFormInstance.announcementId = announcementFormObj
                    announcementEventFormInstance.type = eventType[eventNum]
                    announcementEventFormInstance.save()
                    eventNum += 1

                if(additionalEvents != 0):

                    for x in range (additionalEvents - 1):

                        announcementAdditionalEventForm = CreateAnnouncementAdditionalEventForm(
                            request.POST, prefix="announcementAdditionalEventForm" + str(x))
                        announcementAdditionalEventFormInstance = announcementAdditionalEventForm.save(commit=False)
                        announcementAdditionalEventFormInstance.announcementId = announcementFormObj
                        announcementAdditionalEventFormInstance.save()

                return redirect('/announcement/')
            
            if 'newEventBttn' in request.POST:

                additionalEvents = int(request.POST['title']) + 1

                if (additionalEvents!=1):

                    for x in range (additionalEvents-1):

                        datalist.append(CreateAnnouncementAdditionalEventForm (
                            request.POST, prefix="announcementAdditionalEventForm" + str(x)))
                        #context["announcementAdditionalEventForm" + str(x)] = datalist[x]
                        
                datalist.append(CreateAnnouncementAdditionalEventForm (
                    prefix="announcementAdditionalEventForm" + str(additionalEvents -1 )))
                #context["announcementAdditionalEventForm" + str(additionalEvents)] = datalist[additionalEvents - 1]

                context = {
                    'announcementForm': CreateAnnouncementForm (request.POST, prefix="announcementForm"),
                    'scholarshipAnnouncementForm': CreateScholarshipAnnouncementForm (request.POST, prefix="scholarshipAnnouncementForm"),
                    'announcementEventFormInscription': CreateAnnouncementEventForm (request.POST, prefix="announcementEventFormInscription"),
                    'announcementEventFormSelection': CreateAnnouncementEventForm (request.POST, prefix="announcementEventFormSelection"),
                    'announcementEventFormInterview': CreateAnnouncementEventForm (request.POST, prefix="announcementEventFormInterview"),
                    'announcementEventFormPublication': CreateAnnouncementEventForm (request.POST, prefix="announcementEventFormPublication"),
                    "data": datalist,
                    'additionalEvents': additionalEvents,
                    'error':""
                }

                return render(request, 'createAnnouncement.html', context)
            
            if 'deleteEventBttn' in request.POST:

                additionalEvents = int(request.POST['title']) -1

                for x in range (additionalEvents):

                    datalist.append(CreateAnnouncementAdditionalEventForm (
                        request.POST, prefix="announcementAdditionalEventForm" + str(x)))
                    #context["announcementAdditionalEventForm"+ str(x)] = datalist[x]

                context= {
                    'announcementForm': CreateAnnouncementForm (request.POST, prefix="announcementForm"),
                    'scholarshipAnnouncementForm': CreateScholarshipAnnouncementForm (request.POST, prefix="scholarshipAnnouncementForm"),
                    'announcementEventFormInscription': CreateAnnouncementEventForm (request.POST, prefix="announcementEventFormInscription"),
                    'announcementEventFormSelection': CreateAnnouncementEventForm (request.POST, prefix="announcementEventFormSelection"),
                    'announcementEventFormInterview': CreateAnnouncementEventForm (request.POST, prefix="announcementEventFormInterview"),
                    'announcementEventFormPublication': CreateAnnouncementEventForm (request.POST, prefix="announcementEventFormPublication"),
                    "data": datalist,
                    'additionalEvents':additionalEvents,
                    'error':""
                }

                return render(request, 'createAnnouncement.html', context)
        
        except Exception as ex:

            error= {str(ex)}
            additionalEvents= int(request.POST['title'])

            for x in range (additionalEvents):

                datalist.append(CreateAnnouncementAdditionalEventForm (
                    request.POST, prefix="announcementAdditionalEventForm" + str(x)))
                #context["announcementAdditionalEventForm" + str(x)] = datalist[x]

            context = {
                'announcementForm': CreateAnnouncementForm (request.POST, prefix="announcementForm"),
                'scholarshipAnnouncementForm': CreateScholarshipAnnouncementForm (request.POST, prefix="scholarshipAnnouncementForm"),
                'announcementEventFormInscription': CreateAnnouncementEventForm (request.POST, prefix="announcementEventFormInscription"),
                'announcementEventFormSelection': CreateAnnouncementEventForm (request.POST, prefix="announcementEventFormSelection"),
                'announcementEventFormInterview': CreateAnnouncementEventForm (request.POST, prefix="announcementEventFormInterview"),
                'announcementEventFormPublication': CreateAnnouncementEventForm (request.POST, prefix="announcementEventFormPublication"),
                "data": datalist,
                'additionalEvents': additionalEvents,
                'error':error
            }

            return render(
                request, 'createAnnouncement.html', context) 
        

def searchAnnouncement(request):

    today = str(date.today())

    def getAnnouncemnetContext(announcements):


        class announcementTable:


            def __init__(
                    self, scholarshipName, announcementId, type,status):
                self.scholarshipName= scholarshipName
                self.announcementId = announcementId
                self.type = type
                self.status = status


        scholarshipList = []
        scholarshipNames = []
        announcementList = []
        count = 0
        today = str(date.today())
        types = ["Abierta", "Cerrada", "Mixta"]

        for i in announcements:

            status = "Activa"
            typeNum = i.type
            typeStr = types[typeNum]

            scholarshipList.append(
                ScholarshipAnnouncements.objects.filter(announcementId = i.id).values('scholarshipId').get()['scholarshipId'])
            scholarshipNames.append(
                Scholarships.objects.filter(ID = scholarshipList[count]).values('name').get()['name'])

            startingInstcriptionDate = AnnouncementEvent.objects.filter(
                type = "Inscription").filter(announcementId = i.id).values_list('startingDate', flat = True)
            endPublicationDate = AnnouncementEvent.objects.filter(
                type = "Publication").filter(announcementId = i.id).values_list('endDate', flat = True)

            if today < str(startingInstcriptionDate[0]) or today > str(endPublicationDate[0]):
                status="Inactiva"

            announcementList.append(announcementTable(scholarshipNames[count], i.id, typeStr,status))
            count+=1

        return announcementList
    
    def joinQuery(querySets):

        joinedQuerySets = Announcements.objects.none()

        for i in querySets:
            joinedQuerySets = joinedQuerySets | i

        return joinedQuerySets

    announcements = Announcements.objects.all()
    announcementList = getAnnouncemnetContext(announcements)
    context = {
        'announcementSearchForm': CreateSearchAnnouncementForm (request.POST, prefix="announcementSearchForm"),
        'announcements':announcementList,
    }

    if request.method == 'GET':

        return render(
            request, 'searchAnnouncement.html', context)

    else:

        try:

            if 'searchBttn' in request.POST:
                scholarshipName = request.POST["announcementSearchForm-scholarshipName"]
                announcementId = request.POST["announcementSearchForm-announcementId"]
                annoucementType = request.POST["announcementSearchForm-announcementType"]
                annoucementStatus = request.POST["announcementSearchForm-announcementStatus"]
                startingDateStr = request.POST["announcementSearchForm-startingInscriptionDate"]
                endDateStr = request.POST["announcementSearchForm-endInscriptionDate"]
                scholarshipList = []
                announcementsPreList = []
                startDateList = []
                endDateList = []
                flag = False

                if(
                    scholarshipName != "" or announcementId != "" or 
                    annoucementType != "3" or annoucementStatus != "2" or 
                    startingDateStr != "" or endDateStr !=  ""):

                    announcementList = Announcements.objects.none()
                
                    if (scholarshipName != ""):
                        scholarshipList = Scholarships.objects.filter(name = scholarshipName).values_list('ID', flat=True)
                        count = 0
                        hub = []

                        for i in scholarshipList:

                            hub = ScholarshipAnnouncements.objects.filter(
                                scholarshipId= i).values_list('announcementId', flat=True)

                            for m in hub:

                                if (Announcements.objects.filter(id = m).exists()):
                                    announcementsPreList.append(Announcements.objects.filter(id=m))
                                    count+=1

                        joinedQuery = joinQuery(announcementsPreList)
        
                        if flag:
                            announcementList = announcementList.intersection(joinedQuery)
                        else:
                            announcementList = joinedQuery

                        flag = True

                    if (announcementId != ""):
                        announcementsPreList = Announcements.objects.filter(id=announcementId)

                        if flag:
                            announcementList = announcementList.intersection(announcementsPreList)
                        else:
                            announcementList = announcementsPreList

                        flag = True

                    if (annoucementType != "3"):
                        announcementsPreList = Announcements.objects.filter(type=annoucementType)

                        if flag:
                            announcementList = announcementList.intersection(announcementsPreList)
                        else:
                            announcementList = announcementsPreList

                        flag=True

                    if (annoucementStatus != "2"):
                        announcementsPreList = []

                        if (annoucementStatus == "0"):
                            announcementsFirstPreList = AnnouncementEvent.objects.filter(
                                type="Inscription").filter(startingDate__lte = today).values_list('announcementId', flat = True)
                            announcementsSecondPreList = AnnouncementEvent.objects.filter(
                                type="Publication").filter(endDate__gte = today).values_list('announcementId', flat = True)
                            announcementsIdPreList = announcementsFirstPreList.intersection(announcementsSecondPreList)

                            for i in announcementsIdPreList:

                                if (Announcements.objects.filter(id = i).exists()):
                                    announcementsPreList.append(Announcements.objects.filter(id = i))

                            joinedQuery = joinQuery(announcementsPreList)

                        else:
                            announcementsFirstPreList = AnnouncementEvent.objects.filter(
                                type = "Inscription").filter(startingDate__gte = today).values_list('announcementId', flat = True)
                            announcementsSecondPreList = AnnouncementEvent.objects.filter(
                                type = "Publication").filter(endDate__lte = today).values_list('announcementId', flat = True)
                            announcementsIdPreList = announcementsFirstPreList | announcementsSecondPreList

                            for i in announcementsIdPreList:
                                if (Announcements.objects.filter(id = i).exists()):
                                    announcementsPreList.append(Announcements.objects.filter(id = i))

                            joinedQuery= joinQuery(announcementsPreList)

                        if flag:
                            announcementList = announcementList.intersection(joinedQuery)
                        else:
                            announcementList = joinedQuery

                        flag=True

                    if (startingDateStr != ""):

                        startDateList = AnnouncementEvent.objects.filter(
                            type = "Inscription").filter(startingDate__gte = startingDateStr).values_list('announcementId', flat = True)

                        hub = Announcements.objects.none()
                        announcementsPreList=[]

                        for i in startDateList:

                            if (Announcements.objects.filter(id = i).exists()):
                                announcementsPreList.append(Announcements.objects.filter(id = i))

                        joinedQuery = joinQuery(announcementsPreList)
        
                        if flag:
                            announcementList = announcementList.intersection(joinedQuery)
                        else:
                            announcementList = joinedQuery

                        flag = True

                    if (endDateStr != ""):

                        endDateList = AnnouncementEvent.objects.filter(
                            type = "Inscription").filter(endDate__lte = endDateStr).values_list('announcementId', flat = True)

                        hub=Announcements.objects.none()
                        announcementsPreList=[]

                        for i in endDateList:

                            if (Announcements.objects.filter(id = i).exists()):
                                announcementsPreList.append(Announcements.objects.filter(id = i))

                        joinedQuery = joinQuery(announcementsPreList)
        
                        if flag:
                            announcementList = announcementList.intersection(joinedQuery)
                        else:
                            announcementList = joinedQuery

                        flag=True

                    announcementList = getAnnouncemnetContext(announcementList)
                    context = {
                        'announcementSearchForm': CreateSearchAnnouncementForm (request.POST, prefix="announcementSearchForm"),
                        'announcements':announcementList,
                    }

            else:
                context = {
                    'announcementSearchForm': CreateSearchAnnouncementForm (prefix="announcementSearchForm"),
                    'announcements':announcementList,
                }

            return render(
                request, 'searchAnnouncement.html', context)

        except:

            return render(
            request, 'searchAnnouncement.html', context)


