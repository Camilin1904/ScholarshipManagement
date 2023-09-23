from django.db import models

# Create your models here.

class Donors(models.Model):
    name = models.CharField(max_length=100, blank=False)
    ID = models.IntegerField(
        primary_key=True, auto_created=True, serialize=True, unique=True)

class Scholarships(models.Model):
    name = models.CharField(max_length=100, blank=False)
    ID = models.IntegerField(
        primary_key=True, auto_created=True, serialize=True, unique=True)
    description = models.TextField(blank=True)
    donor = models.ForeignKey(Donors, on_delete= models.CASCADE)
    coverage = models.FloatField(blank=False)
    type = models.IntegerField(blank=False)
    requirements = models.TextField(blank=True)

