# Generated by Django 4.2.5 on 2023-10-01 18:54

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('ID', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Scholarships',
            fields=[
                ('ID', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('donor', models.CharField(max_length=100)),
                ('coverage', models.FloatField()),
                ('type', models.IntegerField()),
                ('requirements', models.TextField(blank=True)),
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
                ('announcement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='id_announcement', to='ScholarshipModule.announcement')),
            ],
        ),
    ]
