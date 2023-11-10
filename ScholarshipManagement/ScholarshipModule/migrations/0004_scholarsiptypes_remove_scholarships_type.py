# Generated by Django 4.2.5 on 2023-10-29 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ScholarshipModule', '0003_rename_id_announcementandapplicant_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScholarsipTypes',
            fields=[
                ('scholarship', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='id_Scholarship', serialize=False, to='ScholarshipModule.scholarships')),
                ('unit', models.IntegerField(choices=[(0, 'Porcentage'), (1, 'Dinero'), (2, 'No especificado')], default=2)),
                ('value', models.FloatField()),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='scholarships',
            name='type',
        ),
    ]