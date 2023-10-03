from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

def isValid(query): return query is not None and query != ''

# Create your views here.


def signUp(request):

    if request.method == 'POST':
        # Save the form answers
        form = CreateNewUser(request.POST)
        error = ""
        for field in form:
            # Errors as text
            error = field.errors.as_text
        if form.is_valid():
            # Save user in data base
            user = form.save()
            # Django login method
            login(request, user)
            return redirect('/home')
        else:
            return render(
                request, './HTML/Signin.html', {'form': form, 'error': error})
    else:
        form = CreateNewUser
    return render(
        request, './HTML/Signin.html', {'form': form})

def signOut(request):
    
    logout(request)
    return redirect('/')

def signIn(request):

    error = ''

    if request.method == "POST":
        # For some reason django failes if I save the form in a variable
        # so i saved each answer
        username = request.POST['username']
        password = request.POST['password']
        try:
            # If the user is not found it creates an exception
            user = User.objects.get(username=username)
            # If the username and password match or not the data base will return
            # None or a User object
            user = authenticate(
                request, username=username, password=password)
            if user is not None:
                # If the fields match with the data base then login the user
                login(request, user)
                # Redirect home
                return redirect('/home')
            else:
                # If the data base returns None
                error = 'El usuario o la contraseña son erroneos'
        except:
            # If the username is not found
            error = 'El usuario no existe'

    return render(request, './HTML/login.html', {
            'form': Login,
            'error': error
    })

# The tag will demand the user to login
@login_required(login_url="/login")
def home(request):
    user = request.user
    if user.role == 0:
        return render(request, './HTML/homeAdmin.html')
    elif user.role == 1:
        return render(request, './HTML/homeFinancial.html')
    elif user.role == 2:
        return render(request, './HTML/homePhilanthropy.html')
    else:
        return render(request, './HTML/notAcces.html')


def scholarships(request):
    if request.method == 'GET':
        try:
            del request.session['name']
        except:
            print(0)
        try:
            del request.session['donor_id']
        except:
            print(0)
        try:
            del request.session['min_cov'] 
        except:
            print(0)
        try:
            del request.session['max_cov']
        except:
            print(0)
            
    reqID = request.POST.get('id')
    reqName = request.POST.get('name')
    reqDonor = request.POST.get('donor_id')
    minCov = request.POST.get('min_cov')
    maxCov = request.POST.get('max_cov')
    hasType0 = request.POST.get('type0')
    hasType1 = request.POST.get('type1')
    hasType2 = request.POST.get('type2')
    print("-",hasType0)
    scholarships = Scholarships.objects.all()
    if(not isValid(reqID) and not isValid(reqName) and not isValid(reqDonor)
       and not isValid(minCov) and not isValid(maxCov)):
        try:
            del request.session['id']
        except:
            print(0)
        
    if isValid(reqID):
        try:
            request.session['id'] = reqID
            scholarships = scholarships.filter(ID=reqID)
        except:
            scholarships = None
    else:
        try:
            reqID = request.session.get('id','')
            request.session['id'] = reqID
            scholarships = scholarships.filter(ID=reqID)
        except:
            scholarships = Scholarships.objects.all()
    if isValid(reqName):
        try:
            request.session['name'] = reqName
            scholarships = scholarships.filter(name=reqName)    
        except:
            scholarships = None
    else:
        try:
            del request.session['name']
        except:
            print(0)
    if isValid(reqDonor):
        try:
            request.session['donor_id'] = reqDonor
            scholarships = scholarships.filter(donor=Donors.objects.get(ID=reqDonor))
        except:
            scholarships = None
    else:
        try:
            del request.session['donor_id']
        except:
            print(0)
    if isValid(minCov):
        try:
            request.session['min_cov'] = minCov
            scholarships = scholarships.filter(coverage__gte=minCov)
        except:
            scholarships = None
    else:
        try:
            del request.session['min_cov'] 
        except:
            print(0)
    if isValid(maxCov):
        try:
            request.session['max_cov'] = maxCov
            scholarships = scholarships.filter(coverage__lte=maxCov)
        except:
            scholarships = None
    else:
        try:
            del request.session['max_cov']
        except:
            print(0)
    if hasType0 == 'on':
        try:
            scht0 = scholarships.objects.filter(type = '0')
        except:
            scht0 = scholarships
    else:
        scht0 = scholarships
    if hasType1 == 'on':
        try:
            scht1 = scholarships.objects.filter(type = '1')
        except:
            scht1 = scholarships
    else:
        scht1 = scholarships
    if hasType2 == 'on':
        try:
            scht2 = scholarships.objects.filter(type = '2')
        except:
            scht2 = scholarships
    else:
        scht2 = scholarships
    try:
        scholarships.intersection(scht0,scht1,scht2)
    except:
        print(0)
    reqID = request.session.get('id','')
    reqName = request.session.get('name','')
    reqDonor = request.session.get('donor_id','')
    minCov = request.session.get('min_cov','')
    maxCov = request.session.get('max_cov','')
    return render(request, './HTML/scholarships.html', {'scholarships': scholarships, 
                                                        'id':reqID, 'name':reqName,
                                                        'donor_id':reqDonor, 
                                                        'min_cov':minCov,
                                                        'max_cov':maxCov})


def createScholarships(request):

    if request.method == 'GET':
        return render(request, './HTML/createScholarship.html', {
            'form': CreateScholarshipForm
        })
    else:
        try:
            form = CreateScholarshipForm(request.POST)
            print(form.data)
            form.save()
            return redirect('scholarships')
        except:
            return render(request, './HTML/createScholarship.html', {
                'form': CreateScholarshipForm,
                'error': 'Please provide valid data'
            })