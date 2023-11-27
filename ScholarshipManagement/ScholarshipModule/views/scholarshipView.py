from django.shortcuts import render
from django.shortcuts import redirect
from ScholarshipModule.forms import *
from ScholarshipModule.models import *
from django.contrib.auth.decorators import login_required
import ScholarshipModule.views.isAllowed as allow

#Shows the user all the information of a scholarship
@login_required(login_url="/login")
def scholarshipView(request):
    if(allow.isAllowed(request.user,0) or allow.isAllowed(request.user,2)):
        #fetches the scholarship
        idScholarship = request.session.get("sch")
        scholarship = Scholarships.objects.filter(ID=idScholarship).first()
        if request.method == 'GET':
            #fetches information not available on the scholarship table
            donor = scholarship.donor
            types = ScholarsipTypes.objects.filter(scholarship_id = idScholarship)
            #render
            return render(request, './HTML/scholarshipView.html', {
                'sch': scholarship,
                'donor':donor,
                'types':types
            })
        else:
            return redirect("/scholarships/edit/")
    else: return redirect('home')