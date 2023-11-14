from django.shortcuts import render
from django.shortcuts import redirect
from ScholarshipModule.forms import *
from ScholarshipModule.models import *

#Shows the user all the information of a scholarship
def scholarshipView(request):
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