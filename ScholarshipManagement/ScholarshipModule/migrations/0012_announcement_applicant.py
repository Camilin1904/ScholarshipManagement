# Generated by Django 4.2.5 on 2023-09-26 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ScholarshipModule', '0011_merge_20230926_1504'),
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
                ('announcement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='id_announcement', to='ScholarshipModule.announcement')),
            ],
        ),
    ]