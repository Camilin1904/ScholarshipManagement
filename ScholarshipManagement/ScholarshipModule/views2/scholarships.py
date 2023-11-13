from django.contrib.auth.models import User
from datetime import date
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from ScholarshipModule.forms import *
from ScholarshipModule.models import *
from ScholarshipModule.views2.scholarshipView import scholarshipView

#Summary screen for all scholarships, filters are handled with js
@login_required(login_url="/login")
def scholarships(request):
    if(request.method == "GET"):
        #makes sure all sessions from the creation and edition of a scholarship are clean
        try:
            del request.session['form1']
        except:
            pass
        try:
            del request.session['donor']
        except:
            pass
        try:
            del request.session['typeData']
        except:
            pass
        try:
            del request.session['sch']
        except:
            pass
        try:
            del request.session['mod']
        except:
            pass
        try:
            del request.session['donorID']
        except:
            pass
        
        #Render
        return render(request, './HTML/scholarships.html', {
            'scholarships' : Scholarships.objects.filter(isDeleted=False),
            })
    else:
        request.session["sch"] = request.POST.get("sch")
        return  redirect("/scholarships/view/")
        
    