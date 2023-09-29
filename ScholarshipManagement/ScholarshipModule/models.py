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


class Announcement(models.Model):
        name = models.CharField(max_length=20, blank=False)
        ID = models.IntegerField(
        primary_key=True, auto_created=True, serialize=True, unique=True)

class StatusApplicant(models.IntegerChoices):
        INREVIEW = 0, _('En revisión')
        BENEFICIARY = 1, _('Beneficiario')
        REFUSED = 2, _('No aceptado')

class Applicant(models.Model):
    name = models.CharField(max_length=20, blank=False)
    lastName = models.CharField(max_length=20, blank=False)
    ID = models.IntegerField(
        primary_key=True, auto_created=True, serialize=True, unique=True)
    studentCode = models.CharField(max_length=20, blank=False,unique=True)
    faculty = models.CharField(max_length=20, blank=False)
    major = models.CharField(max_length=20, blank=False)
    semester = models.IntegerField(blank=True, null= True)
    email= models.EmailField(max_length=40, blank=True, unique=True)
    phone = models.IntegerField(blank=True, null=True)

    status = models.IntegerField(default=StatusApplicant.INREVIEW, choices=StatusApplicant.choices)
    announcement= models.ForeignKey(Announcement, 
                related_name="id_announcement", blank=False, null=True, 
                on_delete= models.CASCADE)
