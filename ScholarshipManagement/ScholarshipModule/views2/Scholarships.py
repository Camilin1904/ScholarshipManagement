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

#Summary screen for all scholarships, filters are handled with js
@login_required(login_url="/login")
def scholarships(request):
    #makes sure all sessions from the creation of a scholarship are clean
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
    #Render
    return render(request, './HTML/scholarships.html', {
        'scholarships' : Scholarships.objects.all(),
        'form': FilterScholarshipForm
        })
        
    