# Generated by Django 4.2.5 on 2023-09-24 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScholarshipModule', '0006_alter_donors_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donors',
            name='ID',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True),
        ),
    ]