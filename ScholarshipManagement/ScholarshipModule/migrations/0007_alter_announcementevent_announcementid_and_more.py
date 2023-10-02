# Generated by Django 4.2.5 on 2023-09-27 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ScholarshipModule', '0006_announcementevent_announcementsstudents_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcementevent',
            name='AnnouncementId',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='AnnouncementId3', to='ScholarshipModule.announcements'),
        ),
        migrations.AlterField(
            model_name='announcementsstudents',
            name='announcementId',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='AnnouncementId2', to='ScholarshipModule.announcements'),
        ),
        migrations.AlterField(
            model_name='announcementsstudents',
            name='studentId',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='StudentId2', to='ScholarshipModule.students'),
        ),
        migrations.AlterField(
            model_name='scholarshipannouncements',
            name='announcementId',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='AnnouncementId1', to='ScholarshipModule.announcements'),
        ),
        migrations.AlterField(
            model_name='scholarshipannouncements',
            name='scholarshipId',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='ScholarshipId1', to='ScholarshipModule.scholarships'),
        ),
    ]