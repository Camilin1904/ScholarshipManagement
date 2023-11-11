from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from ..forms import *
from ..models import *
from .IsAllowed import isAllowed

@login_required(login_url="/login")
def typeOfReport(request):

    if not (isAllowed(request.user, 0) | isAllowed(request.user, 2)):
        return redirect("/home")
    
    if request.method == 'POST':
        
        try:
            request.session["type"] = request.POST["type"]
        except:
            del request.session["type"]
            request.session["type"] = request.POST["type"]

        if request.POST["type"] == "1":
            return redirect("/filterOfReport")
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