from django.db import models

class Location(models.Model):
    locationName = models.CharField(max_length=55)