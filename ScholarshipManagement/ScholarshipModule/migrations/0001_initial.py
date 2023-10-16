# Generated by Django 4.2.5 on 2023-10-16 00:31

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('type', models.IntegerField(choices=[(0, 'Abierta'), (1, 'Cerrada'), (2, 'Mixta')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('ID', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('studentCode', models.CharField(max_length=20, unique=True)),
                ('faculty', models.CharField(max_length=20)),
                ('major', models.CharField(max_length=20)),
                ('semester', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=40, unique=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(0, 'En revisión'), (1, 'Beneficiario'), (2, 'No aceptado')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Donors',
            fields=[
                ('ID', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('role', models.IntegerField(choices=[(0, 'Administrador'), (1, 'Asistente de apoyo financiero'), (2, 'Asistente de filantropia'), (3, 'Ningun rol')], default=3)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Scholarships',
            fields=[
                ('ID', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('coverage', models.FloatField()),
                ('type', models.TextField(choices=[(0, 'Intercambio'), (1, 'Rescate'), (2, 'Sustento')])),
                ('requirements', models.TextField(blank=True)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ScholarshipModule.donors')),
            ],
        ),
        migrations.CreateModel(
            name='ScholarshipAnnouncements',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('announcementId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='AnnouncementId1', to='ScholarshipModule.announcements')),
                ('scholarshipId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ScholarshipId1', to='ScholarshipModule.scholarships')),
            ],
        ),
        migrations.CreateModel(
            name='AnnouncementEvent',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('startingDate', models.DateField()),
                ('endDate', models.DateField()),
                ('type', models.TextField(blank=True, null=True)),
                ('announcementId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='AnnouncementId3', to='ScholarshipModule.announcements')),
            ],
        ),
        migrations.CreateModel(
            name='AnnouncementAndApplicant',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('announcement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='id_announcement', to='ScholarshipModule.announcements')),
                ('applicantID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='id_applicant', to='ScholarshipModule.applicant')),
            ],
        ),
    ]
