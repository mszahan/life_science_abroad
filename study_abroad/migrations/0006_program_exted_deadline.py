# Generated by Django 3.2.11 on 2022-03-22 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_abroad', '0005_auto_20220322_0736'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='exted_deadline',
            field=models.DateField(blank=True, default='2022-08-02'),
            preserve_default=False,
        ),
    ]
