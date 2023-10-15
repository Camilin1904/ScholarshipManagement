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
        try:
            del request.session['name']
        except:
            print(0)
        try:
            del request.session['donor_id']
        except:
            print(0)
        try:
            del request.session['min_cov'] 
        except:
            print(0)
        try:
            del request.session['max_cov']
        except:
            print(0)
        try:
            del request.session['type0']
        except:
            print(0)
        try:
            del request.session['type1']
        except:
            print(0)
        try:
            del request.session['type2']
        except:
            print(0)
            
    reqID = request.POST.get('id')
    reqName = request.POST.get('name')
    reqDonor = request.POST.get('donor_id')
    minCov = request.POST.get('min_cov')
    maxCov = request.POST.get('max_cov')
    hasType0 = request.POST.get('type0')=='on'
    hasType1 = request.POST.get('type1')=='on'
    hasType2 = request.POST.get('type2')=='on'
    flag = hasType0 or hasType1 or hasType2
    print("-",flag)
    scholarships = Scholarships.objects.all()
    if(not isValid(reqID) and not isValid(reqName) and not isValid(reqDonor)
       and not isValid(minCov) and not isValid(maxCov)):
        try:
            del request.session['id']
        except:
            print(0)
        
    if isValid(reqID):
        try:
            request.session['id'] = reqID
            scholarships = scholarships.filter(ID=reqID)
        except:
            scholarships = None
    else:
        try:
            reqID = request.session.get('id','')
            request.session['id'] = reqID
            scholarships = scholarships.filter(ID=reqID)
        except:
            scholarships = Scholarships.objects.all()
    if isValid(reqName):
        try:
            request.session['name'] = reqName
            scholarships = scholarships.filter(name=reqName)    
        except:
            scholarships = None
    else:
        try:
            del request.session['name']
        except:
            print(0)
    if isValid(reqDonor):
        try:
            request.session['donor_id'] = reqDonor
            scholarships = scholarships.filter(donor=Donors.objects.get(ID=reqDonor))
        except:
            scholarships = None
    else:
        try:
            del request.session['donor_id']
        except:
            print(0)
    if isValid(minCov):
        try:
            request.session['min_cov'] = minCov
            scholarships = scholarships.filter(coverage__gte=minCov)
        except:
            scholarships = None
    else:
        try:
            del request.session['min_cov'] 
        except:
            print(0)
    if isValid(maxCov):
        try:
            request.session['max_cov'] = maxCov
            scholarships = scholarships.filter(coverage__lte=maxCov)
        except:
            scholarships = None
    else:
        try:
            del request.session['max_cov']
        except:
            print(0)
    if hasType0:
        try:
            request.session['type0'] = hasType0
            scht0 = scholarships.filter(type = 0)
            print(scht0)
        except:
            scht0 = Scholarships.objects.none()
    else:
        scht0 = Scholarships.objects.none()
        try:
            del request.session['type0']
        except:
            print(0)
    if hasType1:
        try:
            request.session['type1'] = hasType1
            scht1 = scholarships.filter(type = 1)
        except:
            scht1 = Scholarships.objects.none()
    else:
        scht1 = Scholarships.objects.none()
        try:
            del request.session['type1']
        except:
            print(0)
    if hasType2:
        try:
            request.session['type2'] = hasType2
            scht2 = scholarships.filter(type = 2)
        except:
            scht2 = Scholarships.objects.none()
    else:
        scht2 = Scholarships.objects.none()
        try:
            del request.session['type2']
        except:
            print(0)
    if(flag):
        try:
            scholarships = scht0.union(scht1,scht2)
            print('pito')
        except:
            print(0)
    reqID = request.session.get('id','')
    reqName = request.session.get('name','')
    reqDonor = request.session.get('donor_id','')
    minCov = request.session.get('min_cov','')
    maxCov = request.session.get('max_cov','')
    hasType0 = request.session.get('type0', False)
    hasType1 = request.session.get('type1', False)
    hasType2 = request.session.get('type2', False)
    return render(request, './HTML/scholarships.html', {'scholarships': scholarships, 
                                                        'id':reqID, 'name':reqName,
                                                        'donor_id':reqDonor, 
                                                        'min_cov':minCov,
                                                        'max_cov':maxCov, 
                                                        'type0':hasType0,
                                                        'type1':hasType1,
                                                        'type2':hasType2})


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
            announcement = AnnouncementAndApplicant.objects.filter(applicantID=idSt).first().announcement
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
            announcement = AnnouncementAndApplicant.objects.filter(applicantID=idSt).first().announcement
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
            AnnouncementAndApplicant.objects.filter(applicantID=idSt).update(
                announcement=request.POST['announcement'])
        else:
            idAnnouncement = request.POST['announcement']
            announcementGet = Announcements.objects.get(id=idAnnouncement)
            formNew= AnnouncementAndApplicantForm()
            relation=formNew.save(commit=False)
            relation.announcement=announcementGet
            relation.applicantID=applicant
            relation.save()
            
            
        try:
            del request.session['name']
        except:
            print(0)

        return redirect('/searchStudent')

def createApplicants(request):

    if request.method == 'GET':
        return render(request, 'createApplicant.html', {
            'form': CreateApplicantForm,
            'error': ""
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
        if 'edit' in request.POST:
            try:
                del request.session['studentCode']
            except:
                print(0)
       
            print(request.POST)
            request.session['studentCode'] = request.POST["edit"]

            return redirect('/applicants/edit')
        else:
            try:
                
                error = ""
                form = FilterApplicantForm(request.POST)
                
                StudentCodeVerify = False
                AnnouncementVerify = False
                nameVerify = False
                lastNameVerify = False

                StudentCodePost = request.POST['ID']
                AnnouncementPost = request.POST['announcement']
                namePost = request.POST['name']
                lastNamePost = request.POST['lastName']

            
                if namePost !="" and namePost is not None:
                    try: 
                        applicants = applicants.filter(name = namePost)
                    except:
                        nameVerify = True

                if StudentCodePost !="" and StudentCodePost is not None:
                    try:
                        applicants = applicants.filter(studentCode = StudentCodePost)
                    except:
                        StudentCodeVerify = True
                        
                if lastNamePost !="" and lastNamePost is not None:
                    try:
                        applicants = applicants.filter(lastName = lastNamePost)
                    except:
                        lastNameVerify = True

                if AnnouncementPost !="" and AnnouncementPost is not None:
                    try:
                        applicantFromAnnouncement = AnnouncementAndApplicant.objects.filter(announcement_id = AnnouncementPost).values_list('applicantID_id', flat=True)
                        applicants = [applicants.get(ID=id_applicant) for id_applicant in applicantFromAnnouncement]
                    except:
                        AnnouncementVerify = True
                        
                if nameVerify == True:
                    error = "Nombre no encontrado"
                elif AnnouncementVerify == True:
                    error = "Convocatora no encontrada"
                elif lastNameVerify == True:
                    error = "Apellido no encontrado"
                elif StudentCodeVerify == True:
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

                return redirect('/home/')
            
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
            
def searchStudent(request):
    return render(
            request, './HTML/searchStudent.html')