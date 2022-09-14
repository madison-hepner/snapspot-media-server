# Generated by Django 4.1 on 2022-09-14 00:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locationName', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='RoadType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('road_type', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='RoadPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('road_name', models.CharField(max_length=55)),
                ('description', models.CharField(max_length=55)),
                ('locationImg', models.CharField(max_length=55)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='snapspotmediaapi.driver')),
                ('locationId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snapspotmediaapi.location')),
                ('road_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snapspotmediaapi.roadtype')),
            ],
        ),
        migrations.CreateModel(
            name='LocationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_type', models.CharField(max_length=55)),
                ('locationId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snapspotmediaapi.location')),
            ],
        ),
        migrations.CreateModel(
            name='LocationPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('description', models.CharField(max_length=55)),
                ('locationImg', models.CharField(max_length=55)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='snapspotmediaapi.driver')),
                ('locationId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snapspotmediaapi.location')),
                ('location_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snapspotmediaapi.locationtype')),
            ],
        ),
        migrations.CreateModel(
            name='EventPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=55)),
                ('description', models.CharField(max_length=55)),
                ('date', models.DateTimeField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='snapspotmediaapi.driver')),
                ('locationId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snapspotmediaapi.location')),
                ('location_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snapspotmediaapi.locationtype')),
            ],
        ),
        migrations.AddField(
            model_name='driver',
            name='locationId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snapspotmediaapi.location'),
        ),
        migrations.AddField(
            model_name='driver',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
