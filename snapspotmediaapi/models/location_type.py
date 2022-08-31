from django.db import models
from .location import Location

class LocationType(models.Model):
    locationId = models.ForeignKey(Location, on_delete=models.CASCADE)
    location_type = models.CharField(max_length=55)