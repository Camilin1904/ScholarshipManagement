from django.shortcuts import render
from django.shortcuts import redirect
from ..forms import *
from ..models import *
from django.http import HttpResponse

    
def viewApplicant(request):
    studentCodeSt = request.session.get('studentCode')
    applicant = Applicant.objects.filter(studentCode = studentCodeSt)
    idSt = applicant.first().ID

    try:
        announcement = AnnouncementAndApplicant.objects.filter(applicant=idSt).first().announcement.id
        announNoDeleted = AnnouncementAndApplicant.objects.get(applicant=idSt)
        if announNoDeleted.deleted == True:
            announcement = None
    except:
        announcement = None

    if request.method == 'GET':
        return render(request,'./HTML/viewApplicant.html',{'applicant':applicant,
                                                           'announcement':announcement, 'error': ''})
    else:
        if 'back' in request.POST:
            return redirect("/searchStudent/")
        elif 'edit' in request.POST:
       
            print(request.POST)
            request.session['studentCode'] = request.POST['edit']

            return redirect('/applicants/edit')
        elif 'delete' in request.POST:
            applicantDelete = Applicant.objects.get(studentCode = studentCodeSt)
            applicantDelete.deleted = True
            if announcement == None:
                applicantDelete.save()
            else:
                announNoDeleted.deleted = True
                announNoDeleted.save()
                applicantDelete.save()

           

            return redirect("/searchStudent/")