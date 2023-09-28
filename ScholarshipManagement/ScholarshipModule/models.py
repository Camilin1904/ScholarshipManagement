from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager

# Create your models here.


class Scholarships(models.Model):


    name = models.CharField(max_length=100, blank=False)
    ID = models.IntegerField(
        primary_key=True, auto_created=True, serialize=True, unique=True)
    description = models.TextField(blank=True)
    donor = models.CharField(max_length=100, blank=False)
    coverage = models.FloatField(blank=False)
    type = models.IntegerField(blank=False)
    requirements = models.TextField(blank=True)

class Applicant(models.Model):
    studentCode = models.CharField(max_length=11,unique=True,blank=False)
    ID = models.IntegerField(
        primary_key=True, auto_created=True, serialize=True, unique=True)
    name = models.CharField(max_length=20,blank=False)
    lastName = models.CharField(max_length=20,blank=False)
    school = models.CharField(max_length=30,blank=False)
    career = models.CharField(max_length=30,blank=False)
    semester = models.IntegerField(blank=True)
    email = models.CharField(max_length=40,blank=True)
    phone = models.CharField(max_length=10,blank=True)  


#Inheritance from an abstract class
class User(AbstractBaseUser):

    
    #It truly is the email, but I'll save it as username for now
    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=30)
    class Role(models.IntegerChoices):
        ADMIN = 0, _('Administrador')
        FINANCIAL = 1, _('Asistente de apoyo financiero')
        PHILANTROPHY = 2, _('Asistente de filantropia')
        NONE = 3, _('Ningun rol')

    role = models.IntegerField(default=Role.NONE, choices=Role.choices)
    #Django needs me to tell him the new name of the user name fiel for the class
    USERNAME_FIELD = 'username'
    #To avoid errors
    REQUIRED_FIELDS = []
    #It is a Django class that acts as a bridge between database queries and Django models
    objects = UserManager()
