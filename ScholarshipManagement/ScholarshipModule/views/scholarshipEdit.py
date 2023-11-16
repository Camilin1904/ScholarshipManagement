from django.forms import formset_factory
from django.shortcuts import render
from django.shortcuts import redirect
from ScholarshipModule.forms import *
from ScholarshipModule.models import *

#base screen and path chooser
def scholarshipEdit(request):

    #scholarship to be edited
    idScholarship = request.session['sch']
    scholarship = Scholarships.objects.get(ID=idScholarship)

    if request.method == 'GET':
        #tries to display the modified donor, if it wasn't, puts the actual donor
        try:
            donorID = request.session.get("donorID")
            donor = Donors.objects.get(ID = donorID)
        except:
            donor = scholarship.donor
            
        #tries to display the modified types, if it wasn't, puts the actual types
        try:
            types = request.session['typeData']
        except:
            types = ScholarsipTypes.objects.filter(
                                            scholarship_id = idScholarship).values()
        
        #loads the current info into the form
        try:
                form = EditScholarshipForm(initial = {
                    "ID": scholarship.ID,
                    "name":scholarship.name,
                    "description":scholarship.description,
                    "requirements":scholarship.requirements
                })
        except Exception as e:
            #failsafe for unexpected error
            print(e)
            form = EditScholarshipForm
        #render
        return render(request, './HTML/scholarshipEdit.html', {
            'form':form,
            'donor':donor,
            'types':types
        })
    else:
        #dir is an invisible input used to know where to be sent
        dir = request.POST.get("dir")
        #if the user decides to change the donor
        if(dir == "donor"):
            request.method = "GET"
            return editDonor(request)
        #if the user decides to change the type
        if(dir == "type"):
            request.method = "GET"
            return editTypes(request)
        #in case they are returning from one of the auxiliary screens
        dID = request.POST.get("select")
        types = request.POST.get("screen")
        #new donor
        if(dID != None):
            request.session["donorID"] = dID
            request.method = "GET"
            return scholarshipEdit(request)
        #modified types
        if(types != None):
            
            return editTypes(request)
        
        #if no other return happened, then the user must have decided to save
        return saveIntoDatabase(request)
    
#send user the the screen with all donors
def editDonor(request):
    #get
    if request.method == 'GET':
        return render(request, './HTML/searchDonor.html', {
            'donors' : Donors.objects.all(),
            'meter': False
            })
        
# sends the user to the screen where they may modify the current types
def editTypes(request):
    #gets the scholarship
    idScholarship = request.session['sch']
    types = request.session.get(
            "typeData",
            ScholarsipTypes.objects.filter(scholarship_id = idScholarship).values())
    typesForm = list()
    #creates a dictionary for each type in the data base
    for t in types:
        typesForm.append(SchTypeCreationForm(initial = {
            'unit':t['unit'],
            'value':t['value'],
            'type':t['type']
        }))
    if request.method == 'GET':
        #get
        return render(request, './HTML/createTypes.html', {
            'forms': typesForm,
            'meter': False
            })
    else:
        #Saves the information of all types
        unitList = request.POST.getlist('unit')
        valueList = request.POST.getlist('value')
        typeList = request.POST.getlist('type')
        #Creates a matrix so that this lists may be saved in one session
        formDataList = list()
        for n in range(len(unitList)):
            #temporary fix to make it impossible to put percentages over 100
            if float(unitList[n]) == 0 and float(valueList[n]) > 100:
                valueList[n] = 100
            sub = {'unit':unitList[n],'value':valueList[n],'type':typeList[n]}
            formDataList.append(sub)
        #The session is created
        request.session['typeData'] = formDataList
        request.session['mod']= True
        #Change of screen
        request.method = 'GET'
        return scholarshipEdit(request)
    
    
#Organizer for session data, creates the entries in the data base
def saveIntoDatabase(request):
    #fetches the session data
    idScholarship = request.session.get('sch')
    scholarship = Scholarships.objects.get(ID=idScholarship)
    donorID = request.session.get('donorID',scholarship.donor.ID)
    oldTypes = ScholarsipTypes.objects.filter(scholarship_id = idScholarship)
    types = request.session.get('typeData', oldTypes.values())
    
    #creates the scholarship
    Scholarships.objects.filter(ID=idScholarship).update(name=request.POST['name'],
                                                        description=request.POST['description'],
                                                        requirements=request.POST['requirements'],
                                                        donor = Donors.objects.get(ID=donorID))
        
    #As there are an indefinate number of types, they are handled in a loop
    if request.session.get('mod', False):
        
        for t in oldTypes:
            t.delete()
            
        for n in types:
            #list zero of matrix types contains the unit of the type
            #list one of matrix types contains the value
            #list two of matrix types contains the type descriptor known as type
            ScholarsipTypes.objects.create(
                scholarship=Scholarships.objects.get(ID=idScholarship), 
                unit=n['unit'], 
                value=n['value'], 
                type=n['type'])

        
    #returns to the summary screen for all scholarships
    return redirect('viewScholarship')
    