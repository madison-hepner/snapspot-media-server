# Generated by Django 4.1 on 2022-09-07 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snapspotmediaapi', '0002_eventpost_time_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpost',
            name='time_date',
            field=models.DateTimeField(verbose_name=''),
        ),
    ]