# Generated by Django 4.2.3 on 2023-12-10 09:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0003_alter_userprofile_gender_exerciselog'),
    ]

    operations = [
        migrations.AddField(
            model_name='exerciselog',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]