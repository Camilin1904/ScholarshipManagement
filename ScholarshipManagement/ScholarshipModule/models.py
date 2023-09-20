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

class User(models.Model):
    id = models.CharField(max_length=30, primary_key=True, null=False, unique=True)
    password = models.CharField(max_length=20, null=False)
    name = models.CharField(max_length=20)
    last_Name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)

    class Role(models.IntegerChoices):
        ADMIN = 0, _('Administrador')
        FINANCIAL = 1, _('Asistente de apoyo financiero')
        PHILANTROPHY = 2, _('Asistente de filantropia')
        NONE = 3, _('Ningun rol')

    role = models.IntegerField(default=Role.NONE, choices=Role.choices)
