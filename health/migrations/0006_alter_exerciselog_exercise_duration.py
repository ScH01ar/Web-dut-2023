# Generated by Django 4.2.3 on 2023-12-10 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0005_alter_exerciselog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exerciselog',
            name='exercise_duration',
            field=models.IntegerField(),
        ),
    ]