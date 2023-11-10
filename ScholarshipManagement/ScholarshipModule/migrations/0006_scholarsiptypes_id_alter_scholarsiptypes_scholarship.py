# Generated by Django 4.2.5 on 2023-11-06 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ScholarshipModule', '0005_remove_scholarships_coverage'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarsiptypes',
            name='ID',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='scholarsiptypes',
            name='scholarship',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='id_Scholarship', to='ScholarshipModule.scholarships'),
        ),
    ]