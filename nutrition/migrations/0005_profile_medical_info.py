# Generated by Django 3.0.1 on 2019-12-25 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0004_program_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='medical_info',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='nutrition.MedicalInfo'),
            preserve_default=False,
        ),
    ]
