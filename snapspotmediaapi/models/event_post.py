# from django.db import models
# from .location import Location
# from .location_type import LocationType
# from .driver import Driver


# class LocationPost(models.Model):
#     event_name = models.CharField(max_length=55)
#     description = models.CharField(max_length=55)
#     locationId = models.ForeignKey(Location, on_delete=models.CASCADE)
#     location_type = models.ForeignKey(LocationType, on_delete=models.CASCADE)
#     driver = models.ForeignKey(Driver, on_delete=models.DO_NOTHING)
