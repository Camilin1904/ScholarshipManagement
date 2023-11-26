from django.forms import formset_factory
from django.shortcuts import render
from django.shortcuts import redirect
from ScholarshipModule.forms import *
from ScholarshipModule.models import *
from django.contrib.auth.decorators import login_required
import ScholarshipModule.views.isAllowed as allow

#marks a scholarship as deleted
@login_required(login_url="/login")
def deleteScholarship(request):
    if(allow.isAllowed(request.user,0) or allow.isAllowed(request.user,1)):
        sch = request.session["sch"]
        
        Scholarships.objects.filter(ID=sch).update(isDeleted = True)
        schAnn = ScholarshipAnnouncements.objects.filter(scholarshipId = sch)
        schAnn.update(archived=True)
        for n in schAnn:
            print("aaaaaaaaaaa")
            id = n.announcementId.id
            Announcements.objects.filter(id=id).update(archived = True)
        return redirect('scholarships')
    else: return redirect('home')