# Generated by Django 4.2.5 on 2023-10-03 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='species',
            name='planet',
            field=models.CharField(default='Earth', max_length=100),
            preserve_default=False,
        ),
    ]