from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..forms import *
from ..models import *



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
    eventsList2 = AnnouncementEvent.objects.filter(announcementId__in = announcementList).order_by('startingDate')
    eventsList3 = AnnouncementEvent.objects.filter(announcementId__in = announcementList).order_by('endDate')
    counter=0
    counter2=0

    calendarEvents = []

    for count in range(3):

        try:
            event = eventsList2[counter]
            event2 = eventsList3[counter2]

            if event.startingDate >= event2.endDate:

                calendarEvents.append(formatedEvent(
                    event2, "Finalización de "))
                counter2+=1

            else:
                calendarEvents.append(formatedEvent(
                    event, "Inicio de "))
            counter+=1

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
