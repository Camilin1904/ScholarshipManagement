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
    reqID = request.GET.get('id')
    reqName = request.GET.get('name')
    reqDonor = request.GET.get('donor_id')
    minCov = request.GET.get('min_cov')
    maxCov = request.GET.get('max_cov')
    scholarships = Scholarships.objects.all()
    if isValid(reqID):
        try:
            scholarships = scholarships.filter(ID=reqID)
        except:
            scholarships = None
    if isValid(reqName):
        try:
            scholarships = scholarships.filter(name=reqName)
        except:
            scholarships = None
    if isValid(reqDonor):
        try:
            scholarships = scholarships.filter(donor=Donors.objects.get(ID=reqDonor))
        except:
            scholarships = None
    if isValid(minCov):
        try:
            scholarships = scholarships.filter(coverage__gte=minCov)
        except:
            scholarships = None    
    if isValid(maxCov):
        try:
            scholarships = scholarships.filter(coverage__lte=maxCov)
        except:
            scholarships = None
    return render(request, './HTML/scholarships.html', {'scholarships': scholarships})


def createScholarships(request):

    if request.method == 'GET':
        return render(request, './HTML/createScholarship.html', {
            'form': CreateScholarshipForm
        })
    else:
        try:
            form = CreateScholarshipForm(request.POST)
            form.save()
            return redirect('scholarships')
        except:
            return render(request, './HTML/createScholarship.html', {
                'form': CreateScholarshipForm,
                'error': 'Please provide valid data'
            })