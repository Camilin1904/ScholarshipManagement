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


@login_required(login_url="/login")
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
        screen = request.POST.get('screen')
        
        if screen=='summary':
            return saveIntoDatabase(request)
        
        if screen=='types':
            print("me cago en todo")
            return createTypes(request)

        elif screen=='donor':
            return searchDonor(request)
        form = CreateScholarshipForm(request.POST)
        request.session['form1'] = form.data

        request.method = 'GET'
        return searchDonor(request)
            

def searchDonor(request):
    print(request.method)
    if request.method == 'GET':
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
    
    print(request.method)
    typesFormSet = formset_factory(SchTypeCreationForm, can_delete=True)
    if request.method == 'GET':
        print("aaaaaaaaa")
        request.session['flag2'] = True
        return render(request, './HTML/createTypes.html', {
            'forms': typesFormSet
            })
    else:
        print("wut")
        request.session['flag2'] = False
        unitList = request.POST.getlist('form-0-unit')
        valueList = request.POST.getlist('form-0-value')
        typeList = request.POST.getlist('form-0-type')
        formDataList = list()
        formDataList.append(unitList)
        formDataList.append(valueList)
        formDataList.append(typeList)
        request.session['typeData'] = formDataList
        request.method = 'GET'
        print("ass", unitList)
        return createScholarshipsSC4(request)
        
        
    
def createScholarshipsSC4(request):

    if request.method == 'GET':

        form  = request.session.get('form1',CreateScholarshipForm)

        donorID = request.session.get('donor')
        donor = Donors.objects.get(ID = donorID)
        types = request.session.get('typeData')
 
        tnum = len(types[0])
        a = list()
        for i in range(tnum): a.append(i)

        return render(request, './HTML/summaryScreen.html', {
            'ID': form['ID'],
            'name': form['name'],
            'description':form['description'],
            'requirements': form['requirements'],
            'donor':donor,
            'types':types,
            'amount':a
        })
    else:
        try:
            
            return searchDonor(request)
        except:
            return render(request, './HTML/createScholarship.html', {
                'form': CreateScholarshipForm,
                'error': 'Please provide valid data'
            })


def saveIntoDatabase(request):
    baseData = request.session.get('form1')
    donorID = request.session.get('donor')
    types = request.session.get('typeData')
    Scholarships.objects.create(ID=baseData['ID'], name=baseData['name'], 
                                description=baseData['description'], 
                                requirements=baseData['requirements'], 
                                donor=Donors.objects.get(ID=donorID))
    
    for n in range(len(types[0])):
        ScholarsipTypes.objects.create(scholarship=Scholarships.objects.get(ID=baseData['ID']), unit=types[0][n], value=types[1][n], type=types[2][n])
    
    return redirect('scholarships')