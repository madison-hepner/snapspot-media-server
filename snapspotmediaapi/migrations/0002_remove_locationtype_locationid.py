# Generated by Django 4.1 on 2022-08-31 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snapspotmediaapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locationtype',
            name='locationId',
        ),
    ]
