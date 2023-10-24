from django.shortcuts import render
from django.shortcuts import redirect
from .forms import *
from .models import *
from django.http import HttpResponse        

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
        if 'search' in request.POST:
            try:
                del request.session['studentCode']
            except:
                print(0)
       
            print(request.POST)
            request.session['studentCode'] = request.POST["search"]

            return redirect('/view/Student')
        else:
            try:
                
                error = ""
                form = FilterApplicantForm(request.POST)
                
                studentCodeVerify = False
                announcementVerify = False
                nameVerify = False
                lastNameVerify = False

                studentCodePost = request.POST['ID']
                announcementPost = request.POST['announcement']
                namePost = request.POST['name']
                lastNamePost = request.POST['lastName']

                if namePost !="" and namePost is not None:
                    try: 
                        applicants = applicants.filter(name = namePost)
                    except:
                        nameVerify = True

                if studentCodePost !="" and studentCodePost is not None:
                    try:
                        applicants = applicants.filter(studentCode = studentCodePost)
                    except:
                        studentCodeVerify = True

                if lastNamePost !="" and lastNamePost is not None:
                    try:
                        applicants = applicants.filter(lastName = lastNamePost)
                    except:
                        lastNameVerify = True

                if announcementPost !="" and announcementPost is not None:
                    try:
                        applicant_ids = AnnouncementAndApplicant.objects.filter(announcement_id = announcementPost)
                        applicant_ids = applicant_ids.values_list('applicant_id', flat=True)
                        applicants = [applicants.get(ID=id_applicant) for id_applicant in applicant_ids]
                    except:
                        announcementVerify = True

                if nameVerify == True:
                    error = "Nombre no encontrado"
                elif announcementVerify == True:
                    error = "Convocatora no encontrada"
                elif lastNameVerify == True:
                    error = "Apellido no encontrado"
                elif studentCodeVerify == True:
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