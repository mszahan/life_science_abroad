# Generated by Django 3.2.11 on 2022-03-22 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_abroad', '0008_auto_20220322_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarship',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
    ]
