from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from ..forms import *
from ..models import *
from django.http import HttpResponse
import xlwt
from xlwt import XFStyle
from .isAllowed import isAllowed
from django.db.models import Q

@login_required(login_url="/login")
def reportResume(request):

    if not (isAllowed(request.user, 0) | isAllowed(request.user, 2)):
        return redirect("/home")

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

        objects = AnnouncementAndApplicant.objects.select_related('applicant').filter(deleted = 0)

        if len(studentCode) != 0:
            objects = objects.filter(applicant_id__studentCode__contains = studentCode)

        if len(announcementId) != 0:
            objects = objects.filter(announcement_id__id__contains = announcementId)

        if len(semesters) != 0:
            objects = objects.filter(applicant_id__semester__in = semesters)

        if len(careers) != 0:
            objects = objects.filter(applicant_id__major__in = careers)

        if len(faculties) != 0:
            objects = objects.filter(applicant_id__faculty__in = faculties)

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

    elif objectOfReport == "2":
        
        if len(filters) == 0 :
            scholarshipId = []
            scholarship = []
            announcementId = []

        else:
            scholarshipId = filters[0]
            scholarship = filters[1]
            announcementId = filters[2]

        objects = ScholarshipAnnouncements.objects.select_related('scholarshipId').filter(Q(scholarshipId__isDeleted = 0) & Q(announcementId__archived = 0))

        if len(scholarshipId) > 0:
            objects = objects.filter(scholarshipId__ID__contains = scholarshipId)

        if len(scholarship) > 0:
            objects = objects.filter(scholarshipId__name__contains = scholarship)

        if len(announcementId) > 0:
            objects = objects.filter(announcementId__id__contains = announcementId)

    else:

        if len(filters)==0 :
            scholarship = []
            announcementId = []

            types = []

        else :
            scholarship = filters[0]
            announcementId = filters[1]

            types = filters[2]

        TYPES = [
            'Abierta', 'Cerrada', 'Mixta']
        
        typeCounts = []

        objects = ScholarshipAnnouncements.objects.select_related('scholarshipId').filter(Q(scholarshipId__isDeleted = 0) & Q(announcementId__archived = 0))

        if len(scholarship) > 0:
            objects = objects.filter(scholarshipId__name__contains = scholarship)

        if len(announcementId) > 0:
            objects = objects.filter(announcementId__id__contains = announcementId)

        if len(types) > 0:
            for i in range(len(types)):
                if types[i] == "Abierta":
                    types[i] = 0
                elif types[i] == "Cerrada":
                    types[i] = 1
                else:
                    types[i] = 2
            objects = objects.filter(announcementId__type__in = types)

        for i in range(0,3):
            typeCounts.append(len(objects.filter(announcementId__type=i)))
    
    if request.method == 'POST':

        workbook = xlwt.Workbook(encoding='utf-8')

        worksheet = workbook.add_sheet('Información')

        date_format = XFStyle()
        date_format.num_format_str = 'dd/mm/yyyy'

        response = HttpResponse(content_type="application/ms-excel")
        response['Content-Disposition'] = 'attachment; filename = university_records.xls'

        row = 0

        col = 0

        if objectOfReport == "1":

            # field names  
            fields = [
                'Nombre', 'Apellido', 'Código de Estudiante', 'Facultad', 'Carrera',
                'Semestre', 'Correo', 'Teléfono', 'Convocatoria', 'Status']  

            for i in range(len(fields)):
                worksheet.write(row, i, fields[i])

            row += 1
            
            for object in objects:
                
                status =-1
                
                if object.applicant.status==0:
                    status = 'En revisión'
                elif object.applicant.status==1:
                    status = 'Beneficiario'
                elif object.applicant.status==2:
                    status = 'No aceptado'
                else:
                    status = 'NA'

                worksheet.write(row, col, object.applicant.name)
                worksheet.write(row, col+1, object.applicant.lastName)
                worksheet.write(row, col+2, object.applicant.studentCode)
                worksheet.write(row, col+3, object.applicant.faculty)
                worksheet.write(row, col+4, object.applicant.major)
                worksheet.write(row, col+5, object.applicant.semester)
                worksheet.write(row, col+6, object.applicant.email)
                worksheet.write(row, col+7, object.applicant.phone)
                worksheet.write(row, col+8, object.announcement.id)
                worksheet.write(row, col+9, status)

                row += 1

            workbook.save(response)

            return response
        
        elif objectOfReport == "2":

            # field names  
            fields = [
                'Id', 'Nombre', 'Descripción', 'Requerimientos', 'Id del donante', 'Nombre del Donante', 'Id Convocatoria'
            ]  

            for i in range(len(fields)):
                worksheet.write(row, i, fields[i])

            row += 1
            
            for object in objects:

                worksheet.write(row, col, object.scholarshipId.ID)
                worksheet.write(row, col+1, object.scholarshipId.name)
                worksheet.write(row, col+2, object.scholarshipId.description)
                worksheet.write(row, col+3, object.scholarshipId.requirements)
                worksheet.write(row, col+4, object.scholarshipId.donor.ID)
                worksheet.write(row, col+5, object.scholarshipId.donor.name)
                worksheet.write(row, col+6, object.announcementId.id)
                
                row += 1

            workbook.save(response)

            return response
        
        else:

            events = AnnouncementEvent.objects.all()

            fields = [
                'Identificador', 'Tipo', 'Beca', 'Inicio de Inscripción', 'Cierre de Inscripción',
                'Inicio de Entrevistas', 'Cierre de Entrevistas', 'Inicio de Selección',
                'Cierre de Selección', 'Inicio de Publicación de Beneficiarios',
                'Cierre de Publicación de Beneficiarios']
            
            for i in range(len(fields)):
                worksheet.write(row, i, fields[i])

            row += 1

            for object in objects:

                announcementType = -1

                if object.announcementId.type==0 :
                    announcementType = "Abierta"
                elif object.announcementId.type==1:
                    announcementType = "Cerrada"
                else:
                    announcementType = "Mixta"
                
                thisEvents = events.filter(announcementId = object.announcementId.id)
                
                worksheet.write(row, col, object.announcementId.id)
                worksheet.write(row, col+1, announcementType)
                worksheet.write(row, col+2, object.scholarshipId.name)
                worksheet.write(row, col+3, thisEvents.get(type = "Inscription").startingDate, date_format)
                worksheet.write(row, col+4, thisEvents.get(type = "Inscription").endDate, date_format)
                worksheet.write(row, col+5, thisEvents.get(type = "Interview").startingDate, date_format)
                worksheet.write(row, col+6, thisEvents.get(type = "Interview").endDate, date_format)
                worksheet.write(row, col+7, thisEvents.get(type = "Selection").startingDate, date_format)
                worksheet.write(row, col+8, thisEvents.get(type = "Selection").endDate, date_format)
                worksheet.write(row, col+9, thisEvents.get(type = "Publication").startingDate, date_format)
                worksheet.write(row, col+10, thisEvents.get(type = "Publication").endDate, date_format)

                row += 1

            workbook.save(response)
            
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
        elif objectOfReport == "2":
            return render(
                request, './HTML/reportResume.html', {
                    'data': objects,
                    'objectOfReport': objectOfReport
                })
        else:
            return render(
                request, './HTML/reportResume.html', {
                    'data': objects,
                    'objectOfReport': objectOfReport,
                    'typeNames' : TYPES,
                    'type': typeCounts
                })
