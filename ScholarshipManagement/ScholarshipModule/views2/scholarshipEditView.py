from django.shortcuts import render
from django.shortcuts import redirect
from ScholarshipModule.forms import *
from ScholarshipModule.models import *

def scholarshipEdit(request):

    idScholarship = request.session['idScholarship']
    scholarship = Scholarships.objects.filter(ID=idScholarship).first()


    if request.method == 'GET':

        name = scholarship.name
        description = scholarship.description
        id = scholarship.ID
        donor = scholarship.donor
        coverage = scholarship.coverage
        type = scholarship.type
        requirements = scholarship.requirements

        form = EditScholarshipForm(initial={'name':name,
                                              'ID':id,
                                              'description':description,
                                              'donor':donor,
                                              'coverage':coverage,
                                              'type':type,
                                              'requirements':requirements})


        return render(request, './HTML/editScholarship.html', {
            'form': form
        })
    else:
        Scholarships.objects.filter(ID=idScholarship).update(name=request.POST['name'],
                                                             description=request.POST['description'],
                                                             coverage=request.POST['coverage'],
                                                             type=request.POST['type'],
                                                             requirements=request.POST['requirements'])

        return redirect('scholarships')