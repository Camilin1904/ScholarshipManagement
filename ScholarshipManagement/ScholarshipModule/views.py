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
from django.http import HttpResponse
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

@login_required(login_url="/login") 
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
                scholarshipIdInt = request.POST['scholarshipAnnouncementForm-scholarshipId']
                scholarshipIdInt = getSubString(scholarshipIdInt)[-1]

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
                scholarshipAnnouncementForm = CreateScholarshipAnnouncementForm()
                scholarshipObjt = Scholarships.objects.filter(ID = scholarshipIdInt).get()
                announcementForm.save()

                announcementFormObj = Announcements.objects.latest('id')

                scholarshipAnnouncementFormInstance = scholarshipAnnouncementForm.save(commit=False)
                scholarshipAnnouncementFormInstance.scholarshipId = scholarshipObjt
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
        
@login_required(login_url="/login")
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

        for i in announcements:

            typeNum = i.type
            typeStr = getAnnouncemenType(typeNum)

            print(i.id)
            scholarshipList.append(
                ScholarshipAnnouncements.objects.filter(announcementId = i.id).values('scholarshipId').get()['scholarshipId'])
            scholarshipNames.append(
                Scholarships.objects.filter(ID = scholarshipList[count]).values('name').get()['name'])

            status= getStatus(i.id)

            announcementList.append(announcementTable(scholarshipNames[count], i.id, typeStr,status))
            count+=1

        return announcementList
    
    def joinQuery(querySets):

        joinedQuerySets = Announcements.objects.none()

        for i in querySets:
            joinedQuerySets = joinedQuerySets | i

        return joinedQuerySets

    announcements = Announcements.objects.filter(archived = 0)
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
                archivedOption = request.POST["announcementSearchForm-archivedSelection"]
                scholarshipList = []
                announcementsPreList = []
                startDateList = []
                endDateList = []
                flag = False

                if(
                    scholarshipName != "" or announcementId != "" or 
                    annoucementType != "3" or annoucementStatus != "2" or 
                    startingDateStr != "" or endDateStr !=  "" or archivedOption != "0"):

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
                                type = "Inscription").filter(startingDate__gt = today).values_list('announcementId', flat = True)
                            announcementsSecondPreList = AnnouncementEvent.objects.filter(
                                type = "Publication").filter(endDate__lt = today).values_list('announcementId', flat = True)
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

                       

                    if (archivedOption != "0"):

                        print("entro")

                        archivedList = Announcements.objects.filter(
                            archived = 1).values_list('id', flat = True)

                        announcementsPreList=[]

                        for i in archivedList:

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

                    return render(
                    request, 'searchAnnouncement.html', context)


            if 'checkBttn' in request.POST:

                request.session['announcementId'] = request.POST['checkBttn']
                return redirect('/announcement/view/')
            

            else:
                context = {
                    'announcementSearchForm': CreateSearchAnnouncementForm (prefix="announcementSearchForm"),
                    'announcements':announcementList,
                }

            return render(
                request, 'searchAnnouncement.html', context)

        except Exception as e:

            raise Exception(e)
            

            return render(
            request, 'searchAnnouncement.html', context)


            
def searchStudent(request):
    return render(
            request, './HTML/searchStudent.html')


def getAnnouncementViewContext(announcementId):

    class translatedEvent:

        def __init__(
                self, type, startingDate, endDate):
            self.type = type
            self.startingDate = startingDate
            self.endDate = endDate


    announcementDict = getAnnouncementInfo(announcementId)

    archivedStatus = "No"
    archivedStatusBttn = "Archivar"

    if announcementDict["archive"] == 1:
        archivedStatus = "Si"
        archivedStatusBttn = "Desarchivar"

    events = announcementDict["events"]
    translatedEvents = []

    event_dict = {'Inscription' : 'Inscripción', 
           'Interview' : 'Entrevista', 
           'Selection' : 'Selección', 
           'Publication' : 'Publicación'}
    
    for event in events:

        try:
            type = event_dict[event.type]
        except KeyError:
            type = event.type

        translatedEvents.append(translatedEvent(type,
                                                event.startingDate,
                                                event.endDate))

    context = {
            'announcementId': announcementDict["id"],
            'type': announcementDict["type"],
            'scholarship': announcementDict["scholarship"],
            'events': translatedEvents,
            'status': announcementDict["status"],
            'archive': archivedStatus,
            'archiveBttn': archivedStatusBttn
        }
    
    return context

@login_required(login_url="/login")
def viewAnnouncement (request):

    announcementId = request.session.get('announcementId')
    announcementDict = getAnnouncementInfo(announcementId)
    context = getAnnouncementViewContext(announcementId)
    archiveNumberFlag = 1

    if announcementDict["archive"] == 1:
        archiveNumberFlag = 0

    if request.method == 'GET':

        return render(
            request, './HTML/viewAnnouncement.html', context)
    else:

        if 'editBttn' in request.POST:
            return redirect('/announcement/edit/')
        
        
        if 'deleteBttn' in request.POST:

            Announcements.objects.filter(id = announcementId).update(archived = archiveNumberFlag)

            context = getAnnouncementViewContext(announcementId)

            return render(
            request, './HTML/viewAnnouncement.html', context)


def getStatus(id):
    today = str(date.today())
    status = "Activa"

    startingInstcriptionDate = AnnouncementEvent.objects.filter(
                type = "Inscription").filter(announcementId = id).values_list('startingDate', flat = True)
    endPublicationDate = AnnouncementEvent.objects.filter(
                type = "Publication").filter(announcementId = id).values_list('endDate', flat = True)

    if today < str(startingInstcriptionDate[0]) or today > str(endPublicationDate[0]):
                status="Inactiva"

    return status


def getAnnouncemenType(typeNum):
    types = ["Abierta", "Cerrada", "Mixta"]
    typeStr = types[typeNum]

    return typeStr

def getAnnouncementInfo(announcementId):

    announcementObjt = Announcements.objects.filter(id = announcementId)
    announcementScholarship = ScholarshipAnnouncements.objects.filter(announcementId = announcementObjt[0].id)
    scholarship =  announcementScholarship[0].scholarshipId 
    announcementEvents = AnnouncementEvent.objects.filter(announcementId = announcementObjt[0].id)

    announcementDict = {
        "id": announcementId,
        "type":getAnnouncemenType(announcementObjt[0].type),
        "scholarship": scholarship,
        "events": announcementEvents,
        "status": getStatus(announcementId),
        "typeNum":announcementObjt[0].type,
        "idObj":announcementObjt[0],
        "archive": announcementObjt[0].archived 
    }

    return announcementDict


@login_required(login_url="/login")
def editAnnouncement (request):

    error = ""

    announcementId = request.session.get('announcementId')
    announcementDict = getAnnouncementInfo(announcementId)
    scholarshipName = announcementDict["scholarship"].name

    announcementForm = CreateAnnouncementForm(initial={'type':announcementDict["typeNum"]}, prefix = "announcementForm")
    scholarshipAnnouncementForm = CreateScholarshipAnnouncementForm(
        initial={'scholarshipId':announcementDict["scholarship"].name + "  (" + str(announcementDict["scholarship"].ID) +
                  ")"}, prefix = "announcementForm")
    announcementEventFormInscription = CreateAnnouncementEventForm(
        initial={'startingDate':announcementDict["events"][0].startingDate,
                 'endDate':announcementDict["events"][0].endDate}, prefix = "announcementEventFormInscription")
    announcementEventFormSelection = CreateAnnouncementEventForm(
        initial={'startingDate':announcementDict["events"][1].startingDate,
                 'endDate':announcementDict["events"][1].endDate}, prefix = "announcementEventFormSelection")
    announcementEventFormInterview = CreateAnnouncementEventForm(
        initial={'startingDate':announcementDict["events"][2].startingDate,
                 'endDate':announcementDict["events"][2].endDate}, prefix = "announcementEventFormInterview")
    announcementEventFormPublication = CreateAnnouncementEventForm(
        initial={'startingDate':announcementDict["events"][3].startingDate,
                 'endDate':announcementDict["events"][3].endDate}, prefix = "announcementEventFormPublication")

    context = {
            'announcementForm': announcementForm,
            'scholarshipAnnouncementForm': scholarshipAnnouncementForm,
            'announcementEventFormInscription': announcementEventFormInscription,
            'announcementEventFormSelection': announcementEventFormSelection,
            'announcementEventFormInterview': announcementEventFormInterview,
            'announcementEventFormPublication':announcementEventFormPublication,
            'newEventForm': CreateAnnouncementAdditionalEventForm(),
            'scholarshipName':scholarshipName,
            'error': error
        }

    if request.method == 'GET':

        return render(
            request, './HTML/editAnnouncement.html', context)
    
    else:

        try:

            if 'saveBttn' in request.POST:

                eventType = [
                    'Inscription','Interview','Selection','Publication']
                today = str(date.today())
                #additionalEvents = int(request.POST['title']) + 1

                scholarshipIdInt = request.POST['announcementForm-scholarshipId']
                scholarshipIdInt = getSubString(scholarshipIdInt)[-1]

                if (not Scholarships.objects.filter(ID = scholarshipIdInt).exists()):

                    raise Exception("La beca seleccionada no está registrada")


                for x in range (3):

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


                    if (initialDate >= endDate):
                        raise Exception("La fecha final debe ser posterior a la fecha incial")
                
                announcementForm = CreateAnnouncementForm(request.POST,prefix="announcementForm")
                scholarshipAnnouncementForm = CreateScholarshipAnnouncementForm(request.POST,prefix="scholarshipAnnouncementForm")

                Announcements.objects.filter(id = announcementId).update(type = request.POST['announcementForm-type'])

                ScholarshipAnnouncements.objects.filter(id = announcementId).update(scholarshipId = scholarshipIdInt)


                events = [
                    "announcementEventFormInscription","announcementEventFormInterview",
                    "announcementEventFormSelection","announcementEventFormPublication"]
                
                eventsType = [
                    "Inscription","Interview",
                    "Selection","Publication"]
                eventNum = 0

                for event in events:

                    AnnouncementEvent.objects.filter(announcementId = announcementId).filter(
                        type = eventsType[eventNum]).update(startingDate = request.POST[event+"-startingDate"],
                                                            endDate = request.POST[event+"-endDate"] )
                

                    eventNum += 1

                return redirect('/announcement/view/')
            
            else:
                return redirect('/announcement/edit/events')

           
        except Exception as ex:

            error = {str(ex)}

            context = {
                'announcementForm': CreateAnnouncementForm (request.POST, prefix="announcementForm"),
                'scholarshipAnnouncementForm': CreateScholarshipAnnouncementForm (request.POST, prefix="announcementForm"),
                'announcementEventFormInscription': CreateAnnouncementEventForm (request.POST, prefix="announcementEventFormInscription"),
                'announcementEventFormSelection': CreateAnnouncementEventForm (request.POST, prefix="announcementEventFormSelection"),
                'announcementEventFormInterview': CreateAnnouncementEventForm (request.POST, prefix="announcementEventFormInterview"),
                'announcementEventFormPublication': CreateAnnouncementEventForm (request.POST, prefix="announcementEventFormPublication"),
                'scholarshipName':scholarshipName,
                'error':error
            }

            return render(
                request,  './HTML/editAnnouncement.html', context) 
        
@login_required(login_url="/login")
def editEvent(request):

    request.session['editFlag'] = True

    announcementId = request.session.get('announcementId')
    announcementDict = getAnnouncementInfo(announcementId)
    scholarshipName = announcementDict["scholarship"].name

    eventsType = [
                "Inscription","Interview",
                "Selection","Publication"]
    
    newEvents=[]

    for event in announcementDict["events"]:
        if event.type not in eventsType:
            newEvent= CreateAnnouncementAdditionalEventForm(initial={'type': event.type,'startingDate':event.startingDate,
                 'endDate':event.endDate})
            
            newEvents.append(newEvent)

    if request.method == 'GET':

        context = {'newEvents': newEvents,
                   'scholarshipName':scholarshipName,
                    'error': ""}

        return render(
            request, './HTML/editEvents.html', context)
    
    else:

        print("2")
        return redirect('/announcement/edit/')

@login_required(login_url="/login")
def createEvent(request):

    announcementId = request.session.get('announcementId')
    announcementDict = getAnnouncementInfo(announcementId)
    eventsType = [
            "Inscription","Interview",
            "Selection","Publication"]

    if request.method == 'POST':

        print(request.POST)
        postDict = request.POST
        eventsCounter = 0
        objInstances = []

        types =  postDict.getlist('type')
        startDates = postDict.getlist('startingDate')
        endDates = postDict.getlist('endDate')
        
        print (types)

        print(postDict.keys())

        if 'type' in postDict.keys():
            print("Entro")

            for type in types:

                startingDate = startDates[eventsCounter]
                print(startingDate)
                endDate = endDates[eventsCounter]
                print(endDate)
                print(type)

                if (type == '' or startingDate == ''  or endDate == '' ):

                    print("error")

                    return render (request, 'HTML/alertBox.html', {'error': "No se pueden guardar campos vacíos"})
                
                form = CreateAnnouncementAdditionalEventForm()

                print(form)
            
                formObjInstance= form.save(commit = False)
                formObjInstance.announcementId = announcementDict["idObj"]
                formObjInstance.type = type
                formObjInstance.startingDate = startingDate
                formObjInstance.endDate = endDate
                objInstances.append(formObjInstance)

                eventsCounter+=1

        AnnouncementEvent.objects.filter(announcementId = announcementId).exclude(type__in = eventsType).delete()
        for obj in objInstances:
            obj.save()

        response = HttpResponse()
        response["HX-Redirect"] = '/announcement/edit/'
        return response

    else:
       
        return render (request, 'HTML/eventForm.html', {'newEventForm': CreateAnnouncementAdditionalEventForm()})
    

def getSubString(str):
    substrings = []
    in_brackets = False
    current_substring = ""
    
    for strItem in str:
        if strItem == "(":
            in_brackets = True
        elif strItem == ")" and in_brackets:
            substrings.append(current_substring)
            current_substring = ""
            in_brackets = False
        elif in_brackets:
            current_substring += strItem
    
    if current_substring:
        substrings.append(current_substring)
    return substrings
