# Generated by Django 4.2.5 on 2023-11-13 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ScholarshipModule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantStateCheck',
            fields=[
                ('ID', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('semester', models.IntegerField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(0, 'En revisión'), (1, 'Beneficiario'), (2, 'No aceptado'), (3, 'NA')], default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('announcementCheck', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='announcementCheck_id', to='ScholarshipModule.announcements')),
                ('applicantCheck', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applicantCheck_id', to='ScholarshipModule.applicant')),
            ],
        ),
    ]