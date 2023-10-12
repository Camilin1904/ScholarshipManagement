from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager

# Create your models here.

class Donors(models.Model):
    name = models.CharField(max_length=100, blank=False)
    ID = models.IntegerField(
        primary_key=True, auto_created=True, serialize=True, unique=True)

class Announcements(models.Model):


    id = models.IntegerField(
        primary_key = True, auto_created = True, serialize = True, unique = True)
    

    class Type(models.IntegerChoices):


        OPEN = 0, _('Abierta')
        CLOSED= 1, _('Cerrada')
        MIXED= 2, _('Mixta')


    type = models.IntegerField(default = Type.CLOSED, choices = Type.choices)


    
class Scholarships(models.Model):


    name = models.CharField(max_length=100, blank=False)
    ID = models.IntegerField(
        primary_key=True, auto_created=True, serialize=True, unique=True)
    description = models.TextField(blank=True)
    donor = models.ForeignKey(Donors, on_delete= models.CASCADE)
    coverage = models.FloatField(blank=False)
    class ScholarshipType(models.IntegerChoices):
        EXCHANGE = 0, _('Intercambio')
        RESCUE = 1, _('Rescate')
        LIVELIHOOD = 2, _('Sustento')
    type = models.IntegerField(choices=ScholarshipType.choices)
    requirements = models.TextField(blank=True)


class ScholarshipAnnouncements(models.Model):


    id = models.IntegerField(
        primary_key = True, auto_created = True, serialize = True, unique = True)
    scholarshipId = models.ForeignKey(
        Scholarships, related_name = "ScholarshipId1", blank = True, null = True, on_delete = models.CASCADE)
    announcementId = models.ForeignKey(
        Announcements, related_name = "AnnouncementId1", blank = True, null = True, on_delete = models.CASCADE)



class AnnouncementEvent(models.Model):


    id = models.IntegerField(
        primary_key = True, auto_created = True, serialize = True, unique = True)
    announcementId = models.ForeignKey(
        Announcements, related_name = "AnnouncementId3", blank = True, null = True, on_delete=models.CASCADE)
    startingDate = models.DateField(blank = False)
    endDate = models.DateField(blank = False)
    type = models.TextField(blank = True, null = True)


   
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
    

class AnnouncementAndApplicant(models.Model):
    id = models.IntegerField(
        primary_key = True, auto_created = True, serialize = True, unique = True)
    announcement= models.ForeignKey(Announcements, 
        related_name="id_announcement", blank=False, null=True, 
        on_delete= models.CASCADE)
    applicantID= models.ForeignKey(Applicant, 
        related_name="id_applicant", blank=False, null=True, 
        on_delete= models.CASCADE)
    
