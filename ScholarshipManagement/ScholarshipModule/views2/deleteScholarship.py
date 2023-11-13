from django.forms import formset_factory
from django.shortcuts import render
from django.shortcuts import redirect
from ScholarshipModule.forms import *
from ScholarshipModule.models import *

def deleteScholarship(request):
    sch = request.session["sch"]
    
    Scholarships.objects.filter(ID=sch).update(isDeleted = True)
    return redirect('scholarships')