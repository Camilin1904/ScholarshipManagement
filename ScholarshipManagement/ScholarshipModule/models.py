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

    archived = models.BooleanField(default = False)


    
class Scholarships(models.Model):


    name = models.CharField(max_length=100, blank=False)
    ID = models.IntegerField(
        primary_key=True, auto_created=True, serialize=True, unique=True)
    description = models.TextField(blank=True)
    donor = models.ForeignKey(Donors, on_delete= models.CASCADE)
    requirements = models.TextField(blank=True)
    isDeleted = models.BooleanField(default=False)


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
        

        IN_REVIEW = 0, _('En revisión')
        BENEFICIARY = 1, _('Beneficiario')
        REFUSED = 2, _('No aceptado')
        NA = 3, _('NA')


class Applicant(models.Model):


    name = models.CharField(max_length=50, blank=False)
    lastName = models.CharField(max_length=50, blank=False)
    ID = models.IntegerField(
        primary_key=True, auto_created=True, serialize=True, 
        unique=True)
    studentCode = models.CharField(
        max_length=20, blank=False,unique=True)
    faculty = models.CharField(max_length=50, blank=False)
    major = models.CharField(max_length=50, blank=False)
    semester = models.IntegerField(blank=True, null= True)
    email= models.EmailField(max_length=50, blank=True, unique=True)
    phone = models.CharField(max_length=20, blank=False, default='None')
    status = models.IntegerField(
        default=StatusApplicant.NA, choices=StatusApplicant.choices)
    image = models.ImageField(upload_to='images/photos', null= True, blank=True, default="")
    deleted = models.BooleanField(default = False)

class ApplicantStateCheck(models.Model):


    ID = models.IntegerField(
        primary_key = True, auto_created = True, serialize = True, 
        unique = True)
    announcementCheck= models.ForeignKey(
        Announcements, related_name="announcementCheck_id", blank=False, 
        null=True, on_delete= models.CASCADE)
    applicantCheck= models.ForeignKey(
        Applicant, related_name="applicantCheck_id", blank=False, 
        null=True, on_delete= models.CASCADE)
    semester = models.IntegerField(blank=True, null= True)
    status = models.IntegerField(
        default=StatusApplicant.IN_REVIEW, choices=StatusApplicant.choices)
    date = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default = False)

class AnnouncementAndApplicant(models.Model):


    ID = models.IntegerField(
        primary_key = True, auto_created = True, serialize = True, 
        unique = True)
    announcement= models.ForeignKey(
        Announcements, related_name="id_announcement", blank=False, 
        null=True, on_delete= models.CASCADE)
    applicant= models.ForeignKey(
        Applicant, related_name="id_applicant", blank=False, 
        null=True, on_delete= models.CASCADE)
    deleted = models.BooleanField(default = False)



class ScholarsipTypes(models.Model):
    
    ID = models.AutoField(primary_key=True)
    
    scholarship = models.ForeignKey(Scholarships, 
                                    related_name="id_Scholarship", blank = False,
                                    on_delete=models.CASCADE, unique=False)
    
    class SchUnit(models.IntegerChoices):

        PERCENTAGE = 0, _('Porcentage')
        MONEY = 1, _('Dinero')
        UNSPECIFIED = 2, _('No especificado')
        
    unit = models.IntegerField(default=SchUnit.UNSPECIFIED, choices=SchUnit.choices)
    value = models.FloatField(blank=False)
    type = models.CharField(max_length=50,blank=False)
    
    
    
    
    
