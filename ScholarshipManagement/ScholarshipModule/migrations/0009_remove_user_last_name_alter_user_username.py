# Generated by Django 4.2.5 on 2023-09-24 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScholarshipModule', '0008_rename_email_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_Name',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]