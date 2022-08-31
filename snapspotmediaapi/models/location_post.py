from django.db import models
from .location import Location
from .location_type import LocationType

class LocationPost(models.Model):
    
    locationId = models.ForeignKey(Location, on_delete=models.CASCADE)
    location_type = models.CharField(max_length=55)