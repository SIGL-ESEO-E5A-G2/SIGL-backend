# Generated by Django 4.2.5 on 2023-11-24 14:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_entreprise_grilleevaluation_opco_tag_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maitrealternance',
            name='ancienEseo',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.TimeField(default=datetime.datetime(2023, 11, 24, 14, 37, 27, 302852)),
        ),
        migrations.AlterField(
            model_name='responsableentreprise',
            name='ancienEseo',
            field=models.BooleanField(default=False),
        ),
    ]