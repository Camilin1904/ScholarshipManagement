from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from ..forms import *
from ..models import *
from .IsAllowed import isAllowed

@login_required(login_url="/login")
def filterOfReport(request):
    if not (isAllowed(request.user, 0) | isAllowed(request.user, 2)):
        return redirect("/home")
    try:
        objectOfReport = request.session.get("object")
    except:
        return redirect("/home")
    
    if request.method == "POST":

        objects = None

        if(objectOfReport == "1"):

            studentCode = request.POST.get("Código de estudiante..")
            announcementId = request.POST.get("Id de la convocatoria..")

            semesters = request.POST.getlist("semester")
            careers = request.POST.getlist("career")
            faculties = request.POST.getlist("faculty")

            filters = [
                studentCode, announcementId, semesters, careers, faculties
            ]
                
        elif(objectOfReport == "2"):
            scholarshipId = request.POST.get("Id de la beca..")
            scholarship = request.POST.get("Nombre de la beca..")
            announcementId = request.POST.get("Id de la convocatoria..")
            
            filters = [
                scholarshipId, scholarship, announcementId
            ]

        else:
            scholarship = request.POST.get("Nombre de la beca..")
            announcementId = request.POST.get("Id de la convocatoria..")

            types = request.POST.getlist("type")

            filters = [
                scholarship, announcementId, types
            ]

        try:
            request.session["filters"] = filters
        except:
            del request.session["filters"]
            request.session["filters"] = filters

        return redirect("/reportResume")

    else:

        if(objectOfReport == "1"):
            form = StudentReportFilter
            titles = ("Nombre", "Apellido", "Carrera", "Facultad", "Semestre")
            objects = AnnouncementAndApplicant.objects.all()
            inputs = ("Código de estudiante..", "Id de la convocatoria..")
        elif(objectOfReport == "2"):
            form = None
            titles = ("Id", "Nombre", "Descripción", "Requerimientos", "Id de la Convocatoria")
            objects = ScholarshipAnnouncements.objects.all()
            inputs = ("Id de la beca..", "Nombre de la beca..", "Id de la convocatoria..")
        else:
            form = AnnouncementReportFilter
            titles = ("Id", "Tipo", "Beca Asociada", "Descripción")
            objects = ScholarshipAnnouncements.objects.all()
            inputs = ("Id de la convocatoria..", "Nombre de la beca..")

        return render(
            request, './HTML/filterOfReport.html', {
                'form': form, 'titles': titles, 'objects' : objects, 'inputs': inputs,
                'objectOfReport': objectOfReport})