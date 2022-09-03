# Generated by Django 4.1 on 2022-08-31 19:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('snapspotmediaapi', '0002_remove_locationtype_locationid'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationtype',
            name='locationId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='snapspotmediaapi.location'),
            preserve_default=False,
        ),
    ]