from django.db import models

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

class Announcements(models.Model):
    id = models.IntegerField(
        primary_key=True, auto_created=True, serialize=True, unique=True)
    studentId=models.IntegerField(blank=False)
    sholarshipId=models.IntegerField(blank=False)
