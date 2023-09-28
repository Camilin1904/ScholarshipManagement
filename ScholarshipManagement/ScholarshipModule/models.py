from django.db import models
from django.utils.translation import gettext_lazy as _

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

    class Type(models.IntegerChoices):
        OPEN =0, _('Abierta')
        CLOSED=1, _('Cerrada')
        MIXED=2, _('Mixta')

    type = models.IntegerField(default=Type.CLOSED, choices=Type.choices)


class Students(models.Model):
    id = models.IntegerField(
        primary_key=True, auto_created=True, serialize=True, unique=True)


class ScholarshipAnnouncements(models.Model):
    id = models.IntegerField(
        primary_key=True, auto_created=True, serialize=True, unique=True)
    scholarshipId= models.ForeignKey(Scholarships, related_name="ScholarshipId1", blank=True, null=True, on_delete=models.CASCADE)
    announcementId= models.ForeignKey(Announcements, related_name="AnnouncementId1",blank=True, null=True, on_delete=models.CASCADE)

class AnnouncementsStudents(models.Model):
    id = models.IntegerField(
        primary_key=True, auto_created=True, serialize=True, unique=True)
    studentId= models.ForeignKey(Students, related_name="StudentId2", blank=True,on_delete=models.CASCADE)
    announcementId= models.ForeignKey(Announcements, related_name="AnnouncementId2",  blank=True,null=True,on_delete=models.CASCADE)

class AnnouncementEvent(models.Model):
    id = models.IntegerField(
        primary_key=True, auto_created=True, serialize=True, unique=True)
    announcementId = models.ForeignKey(Announcements, related_name="AnnouncementId3",blank=True,null=True, on_delete=models.CASCADE)
    startingDate = models.DateField(blank=False)
    endDate = models.DateField(blank=False)

    class EventType(models.IntegerChoices):
        INSCRIPTIONS =0, _('Inscripciones')
        SELECTIONS=1, _('Seleccion')
        INTERVIEWS=2, _('Entrevistas')
        PUBLICATION=3, _('Publicacion')

    type = models.IntegerField(default=EventType.INSCRIPTIONS, choices=EventType.choices, blank=True,null=True)
    
 



   
