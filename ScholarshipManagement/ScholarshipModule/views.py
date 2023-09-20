from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import *
from .models import *

# Create your views here.


def signUp(request):

    if request.method == 'GET':
        return render(request, './HTML/Signin.html', {
            'form': CreateNewUser
        })
    else:

        if request.POST['password1'] == request.POST['password2']:
            # Register user :)
            
            try:
                user = User.objects.create(id=request.POST['id'],
                                                password=request.POST['password1'])
                user.save()
                return redirect('home')
            except IntegrityError:
                return render(request, './HTML/Signin.html', {
                    'form': CreateNewUser,
                    'error': 'El usuario ya existe en la base de datos'
                })
        
        return render(request, './HTML/Signin.html', {
            'form': CreateNewUser,
            'error': 'Lo sentimos pero las contraseñas no coinciden'
        })

def home(request):
    return render(request, './HTML/HomePage.html')


def scholarships(request):
    scholarships = Scholarships.objects.all()
    return render(request, 'scholarships.html', {'scholarships': scholarships})


def createScholarships(request):

    if request.method == 'GET':
        return render(request, 'createScholarship.html', {
            'form': CreateScholarshipForm
        })
    else:
        try:
            form = CreateScholarshipForm(request.POST)
            form.save()
            return redirect('scholarships')
        except:
            return render(request, 'createScholarship.html', {
                'form': CreateScholarshipForm,
                'error': 'Please provide valid data'
            })


def signout(request):
    logout(request)
    return redirect('home')


def signin(request):

    if request.method == 'GET':
        return render(request, './HTML/LoginPage.html', {
            'form': Login
        })
    else:
        user = User.objects.get(id=request.POST['id'])

        if user == None:
            return render(request, './HTML/LoginPage.html', {
                'form': Login,
                'error': 'El usuario no existe'
            })
        elif request.POST['password1']!=user.password:
            return render(request, './HTML/LoginPage.html', {
                'form': Login,
                'error': 'La contraseña es incorrecta'
            })
        else:
            return redirect('home')