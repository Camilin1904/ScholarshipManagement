# Generated by Django 4.2.5 on 2023-09-23 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ScholarshipModule', '0004_alter_scholarships_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donors',
            fields=[
                ('ID', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='scholarships',
            name='ID',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='scholarships',
            name='donor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ScholarshipModule.donors'),
        ),
    ]