# Generated by Django 4.2.3 on 2023-12-10 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0004_exerciselog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exerciselog',
            name='date',
            field=models.DateField(),
        ),
    ]
