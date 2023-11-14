from django.shortcuts import render
from django.shortcuts import redirect
from ..forms import *
from ..models import *
from django.http import HttpResponse   


def stateCheckFilter(request):

    studentCodeSt = request.session.get('studentCode')
    applicant = Applicant.objects.get(studentCode = studentCodeSt)

    try:
        stateCheck = ApplicantStateCheck.objects.filter(applicantCheck = applicant).filter(deleted = False)
        stateCheck2 = ApplicantStateCheck.objects.filter(applicantCheck = applicant).filter(deleted = False)
    except:
        stateCheck = None
        stateCheck2 = None


    if request.method == 'GET':
        return render(
            request, './HTML/searchStateCheck.html', {
                'form': FilterStateCheck,
                'error': "",
                'stateCheck': stateCheck,
                'stateCheck2': stateCheck2
            })
    else:

        if 'all' in request.POST:


            return render(
                request, './HTML/searchStateCheck.html', {
                    'form': FilterStateCheck,
                    'error': "",
                    'stateCheck': stateCheck,
                    'stateCheck2': stateCheck2
                })
        
        elif 'delete' in request.POST:
            
            return render(
                request, './HTML/searchStateCheck.html', {
                    'form': FilterStateCheck,
                    'error': "",
                    'stateCheck': stateCheck,
                    'stateCheck2': stateCheck2
                })


        form= FilterStateCheck(request.POST)
        error = ""

        statusVerify = False
        semesterVerify = False
        announVerify = False

        statusPost = request.POST['status']
        semesterPost = request.POST['semester']
        announPost = request.POST['announcement']

        if statusPost != "" and statusPost is not None:
            try:
                stateCheck = stateCheck.filter(status = statusPost)
            except:
                statusVerify = True

        if semesterPost != "" and semesterPost is not None:
            try:
                stateCheck = stateCheck.filter(semester = semesterPost)
            except:
                semesterVerify = True

        if announPost != "" and announPost is not None:
            try:
                stateCheck = stateCheck.filter(announcementCheck = announPost)
            except:
                announVerify = True

        if statusVerify == True:
            error = "Estado del estudiante no encontrado"
        
        if semesterVerify == True:
            error = "Semestre del estudiante no encontrado"

        if announVerify == True:
            error = "Convocatoria no encontrado"
        

        return render(
            request, './HTML/searchStateCheck.html', {
                'form': form,
                'error': error,
                'stateCheck': stateCheck,
                'stateCheck2': stateCheck2
            })