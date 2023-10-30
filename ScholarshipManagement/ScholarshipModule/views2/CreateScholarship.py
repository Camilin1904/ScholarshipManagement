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
from django.forms import formset_factory
import json

def isValid(query): return query is not None and query != ''

def createScholarshipsSC1(request):

    if request.method == 'GET':
        data  = request.session.get('form1',None)
        form = CreateScholarshipForm
        if data is not None and  len(data)!=0:
            form = CreateScholarshipForm(initial = {
                "ID": data[0],
                "name":data[1],
                "description":data[2],
                "requirements":data[3]
            })
        return render(request, './HTML/createScholarship.html', {
            'form': form
        })
    else:
        #try:
            form = CreateScholarshipForm(request.POST)
            request.session['form1'] = form.changed_data
            print(form.changed_data)
            request.method = 'GET'
            return searchDonor(request)
       # except:
            #return render(request, './HTML/createScholarship.html', {
                #'form': CreateScholarshipForm,
                #'error': 'Please provide valid data'
            #})
            

def searchDonor(request):
    print(request.method)
    if request.method == 'GET':
        return render(request, './HTML/searchDonor.html', {
            'donors' : Donors.objects.all(),
            'form': FilterScholarshipForm
            })
    else:
        request.session['donor'] = request.POST.get('select')
        request.method = 'GET'
        return createTypes(request)
    
def createTypes(request):
    typesFormSet = formset_factory(SchTypeCreationForm, extra=2, can_delete=True)
    if request.method == 'GET':
        return render(request, './HTML/createTypes.html', {
            'forms': typesFormSet
            })
    else:
        formset = typesFormSet(request.POST, request.FILES)
        formDataList = list()
        for item in formset:
            formDataList.append(item.changed_data)
        
        return createScholarshipsSC4(request)
        
        
    
def createScholarshipsSC4(request):

    

    if request.method == 'GET':
        form  = request.session.get('form1',CreateScholarshipForm)
        return render(request, './HTML/createTypes.html', {
            'form': form
        })
    else:
        try:
            form = CreateScholarshipForm(request.POST)
            request.session['form1'] = form
            request.method = 'POST'
            return searchDonor(request)
        except:
            return render(request, './HTML/createScholarship.html', {
                'form': CreateScholarshipForm,
                'error': 'Please provide valid data'
            })