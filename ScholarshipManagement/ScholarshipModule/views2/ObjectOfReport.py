from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from ..forms import *
from ..models import *
from .IsAllowed import isAllowed

@login_required(login_url="/login")
def objectOfReport(request):

    if not (isAllowed(request.user, 0) | isAllowed(request.user, 2)):
        return redirect("/home")

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