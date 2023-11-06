from django.shortcuts import render
from django.shortcuts import redirect
from .forms import *
from .models import *
from django.http import HttpResponse
import io
import csv

def objectOfReport(request):   
    if request.method == 'POST':

        try:
            request.session["object"] = request.POST["object"]
        except:
            del request.session["object"]
            request.session["object"] = request.POST["object"]

        return redirect("/typeOfReport/")
    else:
        return render(
            request, './HTML/objectOfReport.html'
    ) 

def typeOfReport(request):

    if request.method == 'POST':
        
        try:
            request.session["type"] = request.POST["type"]
        except:
            del request.session["type"]
            request.session["type"] = request.POST["type"]

        if request.POST["type"] == "1":
            return redirect("/filterOfReport")
        #DEBO PROGRAMAR ESTA PARTE NOTA PARA ANDRESK
        else:
            filters = []
            try:
                request.session["filters"] = filters
            except:
                del request.session["filters"]
                request.session["filters"] = filters
            return redirect("/reportResume")
    
    else:       

        return render(
            request, './HTML/typeOfReport.html')

def filterOfReport(request):

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
                
        elif(objectOfReport == 2):
            return redirect("/home")
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
        elif(objectOfReport == 2):
            form = StudentReportFilter
            titles = ("Nombre", "Id", "Id del Donante", "Donante", "Convocatorias", "Beneficios")
            objects = ScholarshipAnnouncements.objects.all()
            inputs = ("Nombre de la beca..", "Id de la beca..", "Id del donante..", "Nombre del donante..")
        else:
            form = AnnouncementReportFilter
            titles = ("Id", "Tipo", "Beca Asociada", "Descripción")
            objects = ScholarshipAnnouncements.objects.all()
            inputs = ("Id de la convocatoria..", "Nombre de la beca..")

        return render(
            request, './HTML/filterOfReport.html', {
                'form': form, 'titles': titles, 'objects' : objects, 'inputs': inputs,
                'objectOfReport': objectOfReport})

def reportResume(request):
    try:
        filters = request.session.get("filters")
    except:
        return redirect("/home")
        
    try:
        objectOfReport = request.session.get("object")
    except:
        return redirect("/home")

    
    if objectOfReport == "1":
        if len(filters)==0 :
            studentCode = []
            announcementId = []

            semesters = []
            careers = []
            faculties = []
        else:
            studentCode = filters[0]
            announcementId = filters[1]

            semesters = filters[2]
            careers = filters[3]
            faculties = filters[4]

        objects = AnnouncementAndApplicant.objects.select_related('applicant')

        if len(studentCode) != 0:
            objects = objects.filter(applicant_id__studentCode__contains = studentCode)

        if len(announcementId) != 0:
            objects = objects.filter(announcement_id__id__contains = announcementId)

        if len(semesters) != 0:
            objects.filter(applicant_id__semester__in = semesters)

        if len(careers) != 0:
            objects.filter(applicant_id__major__in = careers)

        if len(faculties) != 0:
            objects.filter(applicant_id__faculty__in = faculties)

        semesterCounts = []
        semesterNames = []

        careerCounts = []
        careerNames = []

        facultyCounts = []
        facultyNames = []

        SEMESTER = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

        CAREER = [
            "Administración de Empresas",
            "Antropología",
            "Biología",
            "Ciencia Política",
            "Comunicación",
            "Derecho",
            "Diseño de Medios Interactivos",
            "Diseño Industrial",
            "Economía y Negocios Internacionales",
            "Finanzas",
            "Ingeniería Bioquímica",
            "Ingeniería de Sistemas",
            "Ingeniería Industrial",
            "Ingeniería Telemática",
            "Licenciatura en Artes",
            "Licenciatura en Ciencias Naturales",
            "Licenciatura en Ciencias Sociales",
            "Licenciatura en Educación Básica Primaria",
            "Licenciatura en Lenguas Extranjeras",
            "Licenciatura en Literatura y Lengua Castellana",
            "Medicina",
            "Mercadeo Internacional y Publicidad",
            "Música",
            "Psicología",
            "Química con Énfasis en Bioquímica",
            "Química Farmacéutica",
            "Sociología"
        ]

        FACULTY = [
            "Ciencias Administrativas y Económicas",
            "Ciencias Humanas",
            "Ingeniería, Diseño y Ciencias Aplicadas",
            "Ciencias de la Salud"
        ]

        for i in SEMESTER:

            if len(objects.filter(applicant_id__semester = i))>0:
                semesterNames.append([i])
                semesterCounts.append(len(objects.filter(applicant_id__semester = i)))

        for i in CAREER:

            if len(objects.filter(applicant_id__major = i))>0:
                careerNames.append([i])
                careerCounts.append(len(objects.filter(applicant_id__major = i)))

        for i in FACULTY:

            if len(objects.filter(applicant_id__faculty = i))>0:
                facultyNames.append([i])
                facultyCounts.append(len(objects.filter(applicant_id__faculty = i)))
    elif objectOfReport == 2:
        return render(
        request, './HTML/reportResume.html', {})
    else:

        if len(filters)==0 :
            studentCode = ""
            announcementId = ""

            semesters = ""
            careers = ""
            faculties = ""
        else :
            scholarship = filters[0]
            announcementId = filters[1]

            types = filters[2]

        TYPES = [
            'Abierta', 'Cerrada', 'Mixta']
        
        typeCounts = []

        objects = ScholarshipAnnouncements.objects.select_related('scholarshipId')

        if scholarship != "":
            objects = objects.filter(scholarshipId__name__contains = scholarship)

        if announcementId != "":
            objects = objects.filter(announcementId__id__contains = announcementId)

        if len(types) != 0:
            for i in range(len(types)):
                if types[i] == "Abierta":
                    types[i] = 0
                elif types[i] == "Cerrada":
                    types[i] = 1
                else:
                    types[i] = 2
            objects.filter(announcementId__type__in = types)

        for i in range(0,3):
            typeCounts.append(len(objects.filter(announcementId__type=i)))
    
    if request.method == 'POST':

        if objectOfReport == "1":

            # field names  
            fields = [
                'Nombre', 'Apellido', 'Código de Estudiante', 'Facultad', 'Carrera',
                'Semestre', 'Correo', 'Teléfono', 'Convocatoria', 'Status']  

            rows = []  

            rows.append(fields) 
            
            for object in objects:
                
                status =-1
                
                if object.applicant.status==0:
                    status = 'En revisión'
                elif object.applicant.status==1:
                    status = 'Beneficiario'
                else:
                    status = 'No aceptado'


                rows.append([
                    object.applicant.name, object.applicant.lastName, object.applicant.studentCode,
                    object.applicant.faculty, object.applicant.major, object.applicant.semester,
                    object.applicant.email, object.applicant.phone, object.announcement.id, status
                    ])

            buffer = io.StringIO()  # python 2 needs io.BytesIO() instead
            wr = csv.writer(buffer, quoting=csv.QUOTE_ALL)
            wr.writerows(rows)
            buffer.seek(0)
            response = HttpResponse(buffer, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=university_records.csv'

            return response
        elif objectOfReport == "2":
            return response
        else:
            # field names  
            fields = [
                'Identificador', 'Tipo', 'Beca', 'Inicio de Inscripción', 'Cierre de Inscripción',
                'Inicio de Entrevistas', 'Cierre de Entrevistas', 'Inicio de Selección',
                'Cierre de Selección', 'Inicio de Publicación de Beneficiarios',
                'Cierre de Publicación de Beneficiarios']  

            rows = []  

            rows.append(fields) 

            events = AnnouncementEvent.objects.all()
            
            for object in objects:

                announcementType = -1

                if object.announcementId.type==0 :
                    announcementType = "Abierta"
                elif object.announcementId.type==1:
                    announcementType = "Cerrada"
                else:
                    announcementType = "Mixta"
                
                thisEvents = events.filter(announcementId = object.announcementId.id)

                rows.append([
                    object.announcementId.id, announcementType, object.scholarshipId.name,
                    thisEvents.get(type = "Inscription").startingDate,
                    thisEvents.get(type = "Inscription").endDate,
                    thisEvents.get(type = "Interview").startingDate,
                    thisEvents.get(type = "Interview").endDate,
                    thisEvents.get(type = "Selection").startingDate,
                    thisEvents.get(type = "Selection").endDate,
                    thisEvents.get(type = "Publication").startingDate,
                    thisEvents.get(type = "Publication").endDate])

            buffer = io.StringIO()  # python 2 needs io.BytesIO() instead
            wr = csv.writer(buffer, quoting=csv.QUOTE_ALL)
            wr.writerows(rows)
            buffer.seek(0)
            response = HttpResponse(buffer, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=university_records.csv'

            return response
    else:
        if objectOfReport == "1":

            return render(
                request, './HTML/reportResume.html', {
                    'data': objects,
                    'objectOfReport': objectOfReport,
                    'semesterNames': semesterNames,
                    'semester': semesterCounts,
                    'careerNames': careerNames,
                    'career': careerCounts,
                    'facultyNames': facultyNames,
                    'faculty': facultyCounts
                })
        elif objectOfReport == 2:
            return render(
                request, './HTML/reportResume.html', {
                    'data': objects
                })
        else:
            return render(
                request, './HTML/reportResume.html', {
                    'data': objects,
                    'objectOfReport': objectOfReport,
                    'typeNames' : TYPES,
                    'type': typeCounts
                })