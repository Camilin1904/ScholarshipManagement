from django.db import models

# Create your models here.

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

