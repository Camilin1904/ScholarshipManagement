# Generated by Django 4.2.5 on 2023-10-15 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ScholarshipModule', '0002_alter_scholarships_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='announcementandapplicant',
            old_name='id',
            new_name='ID',
        ),
        migrations.RenameField(
            model_name='announcementandapplicant',
            old_name='applicantID',
            new_name='applicant',
        ),
    ]