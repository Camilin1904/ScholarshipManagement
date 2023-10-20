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

def isValid(query): return query is not None and query != ''

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


def scholarships(request):
    if request.method == 'GET':
        return render(request, './HTML/scholarships.html', {
            'scholarships' : Scholarships.objects.all(),
            'form': FilterScholarshipForm
            })
    else:
        form = FilterScholarshipForm(request.POST)
        reqID = request.POST.get('id')
        reqName = request.POST.get('name')
        reqDonor = request.POST.get('donor')
        minCov = request.POST.get('minCoverage')
        maxCov = request.POST.get('maxCoverage')
        type = request.POST.getlist('type')
        scholarships = Scholarships.objects.all()
            
        if isValid(reqID):
            try:
                scholarships = scholarships.filter(ID=reqID)
            except:
                scholarships = None
        if isValid(reqName):
            try:
                scholarships = scholarships.filter(name=reqName)    
            except:
                scholarships = None
        if isValid(reqDonor):
            try:
                scholarships = scholarships.filter(donor=Donors.objects.get(ID=reqDonor))
            except:
                scholarships = None
        if isValid(minCov):
            try:
                scholarships = scholarships.filter(coverage__gte=minCov)
            except:
                scholarships = None
        if isValid(maxCov):
            try:
                scholarships = scholarships.filter(coverage__lte=maxCov)
            except:
                scholarships = None
        if len(type)>0:
            print(type)
            schl = list()
            hold = None
            for t in type:
                schl.append(scholarships.filter(type=t))
            print(schl)
            for s in schl:
                if hold is None:
                    hold = s
                else:
                    print(s)
                    hold = hold.union(s)
                    print(hold)
            
            scholarships = hold
                
        
        print(scholarships)
        return render(request, './HTML/scholarships.html', {
            'scholarships' : scholarships,  
            'form': form,
            'id': reqID if reqID != None else ''
        })


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
        try:
            announcement = AnnouncementAndApplicant.objects.filter(applicant=idSt).first().announcement
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
        
        return render(request,'./HTML/editApplicant.html',{'form':form})
    else:
        applicant = Applicant.objects.get(studentCode = studentCodeSt)
        try:
            announcement = AnnouncementAndApplicant.objects.filter(applicant=idSt).first().announcement
        except:
            announcement = None   
        Applicant.objects.filter(studentCode=studentCodeSt).update(name=request.POST['name'],
                                                                   lastName=request.POST['lastName'],
                                                                   faculty=request.POST['faculty'],
                                                                   major=request.POST['major'],
                                                                   semester=request.POST['semester'],
                                                                   email=request.POST['email'],
                                                                   phone=request.POST['phone'],
                                                                   status=request.POST['status'])
        if announcement is not None:
            AnnouncementAndApplicant.objects.filter(applicant=idSt).update(
                announcement=request.POST['announcement'])
        else:
            idAnnouncement = request.POST['announcement']
            announcementGet = None
            try:
                announcementGet = Announcements.objects.get(id=idAnnouncement)
            except:
                print(0)
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
    except:
        announcement = None

    if request.method == 'GET':
        return render(request,'./HTML/viewApplicant.html',{'applicant':applicant,
                                                           'announcement':announcement})
    else:
        if 'back' in request.POST:
            return redirect("/searchStudent/")
        elif 'edit' in request.POST:
       
            print(request.POST)
            request.session['studentCode'] = request.POST['edit']

            return redirect('/applicants/edit')

    

def createApplicants(request):

    if request.method == 'GET':
        return render(request, 'createApplicant.html', {
            'form': CreateApplicantForm,
            'error': ""
        })
    else:
        try:

            
            form = CreateApplicantForm(request.POST)
            error = ""
            postStudentCode = request.POST['studentCode']
            announcementPost = request.POST['announcement']
            postEmail = request.POST['email']

            try:
                verifyEmail= Applicant.objects.get(email = postEmail)
            except: 
                verifyEmail=1

            try:
                verifyStudentCode= Applicant.objects.get(studentCode = postStudentCode)
            except:
                verifyStudentCode=1
      

            try:
                
                
                if verifyStudentCode != 1:
                    error = 'El código de estudiante ya existe'    
                elif verifyEmail !=1:
                    error = 'El email de estudiante ya existe'
                else:
                    error = 'Digite información correctamente'
                form.save()

                if announcementPost == "":
                    error=""
                else: 
                    student = Applicant.objects.get(studentCode = postStudentCode)
                    annuncement=Announcements.objects.get(id=announcementPost)

                    print(student.ID,announcementPost)

                    formNew= AnnouncementAndApplicantForm()
                    relation=formNew.save(commit=False)
                    relation.announcement=annuncement
                    relation.applicant=student
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
        
def filterApplicants(request):

    applicants= None
    applicants = Applicant.objects.all()
    if request.method == 'GET':
        return render(
            request, './HTML/searchStudent.html', {
                'form': FilterApplicantForm,
                'error': "",
                'applicants': applicants
            })
    else:
        if 'search' in request.POST:
            try:
                del request.session['studentCode']
            except:
                print(0)
       
            print(request.POST)
            request.session['studentCode'] = request.POST["search"]

            return redirect('/view/Student')
        else:
            try:
                
                error = ""
                form = FilterApplicantForm(request.POST)
                
                studentCodeVerify = False
                announcementVerify = False
                nameVerify = False
                lastNameVerify = False

                studentCodePost = request.POST['ID']
                announcementPost = request.POST['announcement']
                namePost = request.POST['name']
                lastNamePost = request.POST['lastName']

                if namePost !="" and namePost is not None:
                    try: 
                        applicants = applicants.filter(name = namePost)
                    except:
                        nameVerify = True

                if studentCodePost !="" and studentCodePost is not None:
                    try:
                        applicants = applicants.filter(studentCode = studentCodePost)
                    except:
                        studentCodeVerify = True

                if lastNamePost !="" and lastNamePost is not None:
                    try:
                        applicants = applicants.filter(lastName = lastNamePost)
                    except:
                        lastNameVerify = True

                if announcementPost !="" and announcementPost is not None:
                    try:
                        applicant_ids = AnnouncementAndApplicant.objects.filter(announcement_id = announcementPost)
                        applicant_ids = applicant_ids.values_list('applicant_id', flat=True)
                        applicants = [applicants.get(ID=id_applicant) for id_applicant in applicant_ids]
                    except:
                        announcementVerify = True

                if nameVerify == True:
                    error = "Nombre no encontrado"
                elif announcementVerify == True:
                    error = "Convocatora no encontrada"
                elif lastNameVerify == True:
                    error = "Apellido no encontrado"
                elif studentCodeVerify == True:
                    error = "ID no encontrado"

                return render(
                    request, './HTML/searchStudent.html', {
                        'form': form,
                        'error': error,
                        'applicants': applicants
                    })
            except:
                return render(
                    request, './HTML/searchStudent.html', {
                    'form': form,
                    'error': error
                })       
        
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

            if 'editBttn' in request.POST:

                request.session['annoucementId'] = request.POST['editBttn']
                print(".................")
                return redirect('/announcement/edit/')
            

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


            
def searchStudent(request):
    return render(
            request, './HTML/searchStudent.html')


def editAnnouncement (request):

    announcementId = request.session.get['announcementId']


    context = {
            'announcementForm': CreateAnnouncementForm (prefix="announcementForm"),
            'scholarshipAnnouncementForm': CreateScholarshipAnnouncementForm (prefix="scholarshipAnnouncementForm"),
            'announcementEventFormInscription': CreateAnnouncementEventForm (prefix="announcementEventFormInscription"),
            'announcementEventFormSelection': CreateAnnouncementEventForm (prefix="announcementEventFormSelection"),
            'announcementEventFormInterview': CreateAnnouncementEventForm (prefix="announcementEventFormInterview"),
            'announcementEventFormPublication': CreateAnnouncementEventForm (prefix="announcementEventFormPublication"),
            'error':""
        }

    if request.method == 'GET':

        return render(
            request, './HTML/.html', context)

