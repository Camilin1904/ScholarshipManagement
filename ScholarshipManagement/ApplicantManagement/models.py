from django.db import models


class Applicant:
    studentCode = models.CharField(
        primary_key=True,max_length=11,unique=True)
    ID = models.IntegerField(
        primary_key=True, auto_created=True, serialize=True, unique=True)
    name = models.CharField(max_length=20,blank=False)
    lastName = models.CharField(max_length=20,blank=False)
    school = models.CharField(max_length=30,blank=False)
    career = models.CharField(max_length=30,blank=False)
    semester = models.IntegerField(blank=True)
    email = models.CharField(max_length=40,blank=True)
    phone = models.CharField(max_length=10,blank=True)  

# Create your models here.
