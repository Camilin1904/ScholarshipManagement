from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..forms import *
from ..models import *
from .isAllowed import isAllowed
from django.shortcuts import redirect

@login_required(login_url="/login")
def viewCalendar(request):

    if not (isAllowed(request.user, 0) | isAllowed(request.user, 1) | isAllowed(request.user, 2)):
        return redirect("/home")

    calendarEvents = []

    announcementList = Announcements.objects.filter(archived = 0).values_list('id', flat = True)

    eventsList = AnnouncementEvent.objects.filter(announcementId__in = announcementList)

    for event in eventsList:

        scholarshipId = ScholarshipAnnouncements.objects.filter(
            announcementId = event.announcementId).values_list('scholarshipId', flat = True)[0]
        scholarshipName = Scholarships.objects.filter(
            ID = scholarshipId).values_list('name', flat = True)[0]


        calendarEvents.append(calendarEvent(
            event.type, event.startingDate, event.endDate,scholarshipName))

    context = {
        'eventsList': calendarEvents,
    }

    return render(
            request, './HTML/calendar.html',context)

class calendarEvent:

        def __init__(
            self, type, startingDate, endDate, scholarship):
            self.startingDate= startingDate
            self.endDate = endDate
            self.scholarship = scholarship

            try:

                typeDict = {'Inscription' : "Inscripción" , 
                        'Interview' : "Entrevista", 
                        'Selection' : "Selección", 
                        'Publication' : "Publicación"
                }

                self.type = typeDict[type]

            except KeyError:
                self.type = type