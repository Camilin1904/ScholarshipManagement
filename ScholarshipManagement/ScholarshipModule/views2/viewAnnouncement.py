from datetime import date
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from ..forms import *
from ..models import *
from .searchAnnouncement import *


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
