# Generated by Django 3.2.11 on 2022-03-22 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study_abroad', '0002_alter_university_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='university',
            name='country',
        ),
    ]
