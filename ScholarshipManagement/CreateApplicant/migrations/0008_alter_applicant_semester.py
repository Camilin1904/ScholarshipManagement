# Generated by Django 4.2.5 on 2023-09-25 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CreateApplicant', '0007_alter_applicant_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='semester',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
