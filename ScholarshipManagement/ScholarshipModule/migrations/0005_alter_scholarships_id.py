# Generated by Django 4.2.5 on 2023-09-21 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScholarshipModule', '0004_alter_scholarships_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarships',
            name='ID',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True),
        ),
    ]
