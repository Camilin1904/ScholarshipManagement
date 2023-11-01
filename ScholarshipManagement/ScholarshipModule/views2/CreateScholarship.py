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
        print(data)
        if data is not None and  len(data)<3:
            try:
                form = CreateScholarshipForm(initial = {
                    "ID": data['ID'],
                    "name":data['name'],
                    "description":data['description'],
                    "requirements":data['requirements']
                })
            except:
                form = CreateScholarshipForm
        return render(request, './HTML/createScholarship.html', {
            'form': form
        })
    else:
        try:
            if request.session.get('flag2', False):
                return createScholarshipsSC4(request)
            
            if request.session.get('flag',False):
                return searchDonor(request)
            
            form = CreateScholarshipForm(request.POST)
            request.session['form1'] = form.data
            print('aaa ', request.session.get('form1','pito'))
            
        except:
            return render(request, './HTML/createScholarship.html', {
                'form': CreateScholarshipForm,
                'error': 'Please provide valid data'
            })
        request.method = 'GET'
        return searchDonor(request)
            

def searchDonor(request):
    print(request.method)
    if request.method == 'GET':
        request.session['flag'] = True
        return render(request, './HTML/searchDonor.html', {
            'donors' : Donors.objects.all(),
            'form': FilterScholarshipForm
            })
    else:
        request.session['donor'] = request.POST.get('select')
        print(request.session.get('donor','pito'))
        request.method = 'GET'
        return createTypes(request)
    
def createTypes(request):
    typesFormSet = formset_factory(SchTypeCreationForm)
    if request.method == 'GET':
        del request.session['flag']
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
        return render(request, './HTML/summaryScreen.html', {
            'form': form
        })
    else:
        try:
            request.session['flag2'] = True
            return searchDonor(request)
        except:
            return render(request, './HTML/createScholarship.html', {
                'form': CreateScholarshipForm,
                'error': 'Please provide valid data'
            })