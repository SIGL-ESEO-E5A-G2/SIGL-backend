# Generated by Django 4.2.5 on 2023-11-24 14:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_maitrealternance_ancieneseo_alter_message_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='type',
            field=models.CharField(choices=[('Livrable', 'Livrable'), ('Note', 'Note'), ('Autre', 'Autre')], default='Autre', max_length=10),
        ),
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.TimeField(default=datetime.datetime(2023, 11, 24, 14, 43, 12, 245098)),
        ),
    ]