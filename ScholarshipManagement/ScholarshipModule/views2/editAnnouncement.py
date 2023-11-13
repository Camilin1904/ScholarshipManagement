from datetime import date
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from ..forms import *
from ..models import *
from django.http import HttpResponse
from .createAnnouncement import *
from .viewAnnouncement import *

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

        return redirect('/announcement/edit/')


@login_required(login_url="/login")
def createEvent(request):

    announcementId = request.session.get('announcementId')
    announcementDict = getAnnouncementInfo(announcementId)
    eventsType = [
            "Inscription","Interview",
            "Selection","Publication"]

    if request.method == 'POST':

        postDict = request.POST
        eventsCounter = 0
        objInstances = []
        types =  postDict.getlist('type')
        startDates = postDict.getlist('startingDate')
        endDates = postDict.getlist('endDate')

        if 'type' in postDict.keys():

            for type in types:

                startingDate = startDates[eventsCounter]
                endDate = endDates[eventsCounter]

                if (type == '' or startingDate == ''  or endDate == '' ):

                    return render (request, 'HTML/alertBox.html', {'error': "No se pueden guardar campos vacíos"})
                
                form = CreateAnnouncementAdditionalEventForm()
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
    

