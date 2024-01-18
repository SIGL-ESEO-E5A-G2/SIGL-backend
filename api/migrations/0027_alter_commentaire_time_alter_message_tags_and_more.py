# Generated by Django 4.2.5 on 2024-01-16 20:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_alter_commentaire_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentaire',
            name='time',
            field=models.TimeField(default=datetime.datetime(2024, 1, 16, 20, 34, 28, 814229)),
        ),
        migrations.AlterField(
            model_name='message',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='api.tag'),
        ),
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.TimeField(default=datetime.datetime(2024, 1, 16, 20, 34, 28, 810303)),
        ),
    ]