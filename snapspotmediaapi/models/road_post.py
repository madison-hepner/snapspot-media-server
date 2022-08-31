from django.db import models
from .location import Location
from .driver import Driver
from .road_type import RoadType


class RoadPost(models.Model):
    road_name = models.CharField(max_length=55)
    description = models.CharField(max_length=55)
    locationImg = models.CharField(max_length=55)
    locationId = models.ForeignKey(Location, on_delete=models.CASCADE)
    road_type = models.ForeignKey(RoadType, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.DO_NOTHING)
