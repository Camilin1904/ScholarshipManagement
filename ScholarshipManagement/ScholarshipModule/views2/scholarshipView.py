from django.shortcuts import render
from django.shortcuts import redirect
from ScholarshipModule.forms import *
from ScholarshipModule.models import *


def scholarshipView(request):
    idScholarship = request.session.get("sch")
    scholarship = Scholarships.objects.filter(ID=idScholarship).first()

    if request.method == 'GET':

        donor = scholarship.donor
        types = ScholarsipTypes.objects.filter(scholarship_id = idScholarship)

        return render(request, './HTML/scholarshipView.html', {
            'sch': scholarship,
            'donor':donor,
            'types':types
        })
    else:
        return redirect("/scholarships/edit/")