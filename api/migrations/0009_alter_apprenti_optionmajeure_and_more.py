# Generated by Django 4.2.5 on 2023-11-20 13:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_message_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apprenti',
            name='optionMajeure',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='apprenti',
            name='optionMineure',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.TimeField(default=datetime.datetime(2023, 11, 20, 13, 54, 52, 198473)),
        ),
    ]
