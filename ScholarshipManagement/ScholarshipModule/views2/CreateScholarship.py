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

#Screen one of creation process, base data of a scholarship
#also decides what screen to display if not the first one
@login_required(login_url="/login")
def createScholarshipsSC1(request):

    if request.method == 'GET':
        data  = request.session.get('form1',None)
        form = CreateScholarshipForm
        #If there is any saved data, it is loaded back into the form
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
        #Identifier used to know what screen to display
        screen = request.POST.get('screen')
        #Displays las screen
        if screen=='summary':
            #if anything goes wrong, returns to page one
            try:
                return saveIntoDatabase(request)
            except:
                return render(request, './HTML/createScholarship.html', {
                    'form': CreateScholarshipForm,
                    'error': 'Please provide valid data'
                })
        #Displays The type creation screen
        elif screen=='types':
            return createTypes(request)
        #Displays the donor selection screen
        elif screen=='donor':
            return searchDonor(request)
        #If the screen was the first one, then the info from post 
        #is saved in a session
        form = CreateScholarshipForm(request.POST)
        request.session['form1'] = form.data
        #The screen that follows in the process is donor,
        #therefore the method is accessed as if it were a get,
        #this has the ultimate purpose of using only one url
        #for the creation of scholarships
        request.method = 'GET'
        return searchDonor(request)
            
#Second screen
def searchDonor(request):
    #get
    if request.method == 'GET':
        return render(request, './HTML/searchDonor.html', {
            'donors' : Donors.objects.all(),
            'meter': True
            })
    else:
        #The donor is saved into a session for later use
        request.session['donor'] = request.POST.get('select')
        #must enter next screen as a get
        request.method = 'GET'
        return createTypes(request)
    
    
def createTypes(request):
    typesForm = SchTypeCreationForm()
    listForms = list()
    listForms.append(typesForm)
    if request.method == 'GET':
        #get
        return render(request, './HTML/createTypes.html', {
            'forms': listForms,
            'meter':True
            })
    else:
        #Saves the information of all types
        #It is saved this way as the information per type
        #Is ordered, so, saving it as a list per variable
        #Makes creation smoother
        unitList = request.POST.getlist('unit')
        valueList = request.POST.getlist('value')
        typeList = request.POST.getlist('type')
        #Creates a matrix so that this lists may be saved in one session}
        for n in range(len(unitList)):
            if float(unitList[n]) == 0 and float(valueList[n]) > 100:
                valueList[n] = 100
        formDataList = list()
        formDataList.append(unitList)
        formDataList.append(valueList)
        formDataList.append(typeList)
        #The session is created
        request.session['typeData'] = formDataList
        #Change of screen
        request.method = 'GET'
        return createScholarshipsSC4(request)
        
        
#Summary screen
def createScholarshipsSC4(request):

    if request.method == 'GET':
        #get
        #The information from the sessions is fetched to display all
        #of the information at once
        form  = request.session.get('form1',CreateScholarshipForm)
        donorID = request.session.get('donor')
        donor = Donors.objects.get(ID = donorID)
        types = request.session.get('typeData')
        #Workaround the lack of native number ranges in the version of jinja
        #in django
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
        #failsafe as this method should never be accessed as a post
        return render(request, './HTML/createScholarship.html', {
            'form': CreateScholarshipForm,
            'error': 'Please provide valid data'
        })

#Organizer for session data, creates the entries in the data base
def saveIntoDatabase(request):
    #fetches the session data
    baseData = request.session.get('form1')
    donorID = request.session.get('donor')
    types = request.session.get('typeData')
    #creates the scholarship
    Scholarships.objects.create(ID=baseData['ID'], name=baseData['name'], 
                                description=baseData['description'], 
                                requirements=baseData['requirements'], 
                                donor=Donors.objects.get(ID=donorID))
    #As there are an indefinate number of types, they are handled in a loop
    for n in range(len(types[0])):
        #list zero of matrix types contains the unit of the type
        #list one of matrix types contains the value
        #list two of matrix types contains the type descriptor known as type
        ScholarsipTypes.objects.create(
            scholarship=Scholarships.objects.get(ID=baseData['ID']), 
            unit=types[0][n], 
            value=types[1][n], 
            type=types[2][n])
    #returns to the summary screen for all scholarships
    return redirect('scholarships')