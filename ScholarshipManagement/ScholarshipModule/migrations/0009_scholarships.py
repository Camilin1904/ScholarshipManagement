# Generated by Django 4.2.5 on 2023-09-24 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ScholarshipModule', '0008_delete_scholarships'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scholarships',
            fields=[
                ('ID', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('coverage', models.FloatField()),
                ('type', models.IntegerField()),
                ('requirements', models.TextField(blank=True)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ScholarshipModule.donors')),
            ],
        ),
    ]
