from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..forms import *
from ..models import *
from datetime import date



# The tag will demand the user to login
@login_required(login_url="/login")
def home(request):

    user = request.user

    context = {
            'eventsList': getEventsList(),
    }

    if user.role == 0:
        return render(request, './HTML/homeAdmin.html',context)
    elif user.role == 1:
        return render(request, './HTML/homeFinancial.html',context)
    elif user.role == 2:
        return render(request, './HTML/homePhilanthropy.html',context)
    else:
        return render(request, './HTML/notAcces.html')
    

def getEventsList():

    announcementList = Announcements.objects.filter(archived = 0).values_list('id', flat = True)
    eventsListStart = AnnouncementEvent.objects.filter(
        announcementId__in = announcementList).filter(startingDate__gte = str(date.today())).order_by('startingDate')
    eventsListEnd = AnnouncementEvent.objects.filter(
        announcementId__in = announcementList).filter(endDate__gte = str(date.today())).order_by('endDate')
    counterStart = 0
    counterEnd = 0
    outOfBoundFlag = 0

    calendarEvents = []

    for count in range(3):

        try:
            if outOfBoundFlag != 2:
                try:
                    eventStart = eventsListStart[counterStart]
                except:
                    eventEnd = eventsListEnd[counterEnd]
                    calendarEvents.append(formatedEvent(
                            eventEnd, "Finalización de "))
                    counterEnd+=1
                    outOfBoundFlag = 1

            if outOfBoundFlag != 1:
                try:
                    eventEnd = eventsListEnd[counterEnd]
                except:
                    eventStart = eventsListStart[counterStart]
                    calendarEvents.append(formatedEvent(
                            eventStart, "Inicio de "))
                    counterStart+=1
                    outOfBoundFlag = 2

            if outOfBoundFlag == 0:

                if eventStart.startingDate >= eventEnd.endDate:

                    calendarEvents.append(formatedEvent(
                        eventEnd, "Finalización de "))
                    counterEnd+=1

                else:
                    calendarEvents.append(formatedEvent(
                        eventStart, "Inicio de "))
                    counterStart+=1

        except:
            return calendarEvents
        
    return calendarEvents


class formatedEvent:

        def __init__(
                self, event, prefix):
            
            scholarshipId = ScholarshipAnnouncements.objects.filter(
                announcementId = event.announcementId).values_list('scholarshipId', flat = True)[0]
            scholarshipName = Scholarships.objects.filter(
                ID = scholarshipId).values_list('name', flat = True)[0]

            eventType = event.type

            try:

                typeDict = {'Inscription' : "Inscripción" , 
                        'Interview' : "Entrevista", 
                        'Selection' : "Selección", 
                        'Publication' : "Publicación"
                }

                self.type = typeDict[eventType]

            except KeyError:
                self.type = eventType

            
            if prefix == "Finalización de ":
                self.date = event.endDate

            else :
                self.date = event.startingDate
            
            self.prefix = prefix
            self.scholarship = scholarshipName
