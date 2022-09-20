from django.db import models
from .location import Location
from .location_type import LocationType
from .driver import Driver


class EventPost(models.Model):
    event_name = models.CharField(max_length=55)
    description = models.CharField(max_length=55)
    locationId = models.ForeignKey(Location, on_delete=models.CASCADE)
    location_type = models.ForeignKey(LocationType, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.DO_NOTHING)
    date = models.DateTimeField()
    attendees = models.ManyToManyField(Driver, related_name="attending")

    @property
    def joined(self):
        return self.__joined

    # Setter
    @joined.setter
    def joined(self, value):
        self.__joined = value