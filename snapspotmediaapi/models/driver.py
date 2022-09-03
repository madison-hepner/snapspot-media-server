from django.db import models
from django.contrib.auth.models import User
from .location import Location


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    locationId = models.ForeignKey(Location, on_delete=models.CASCADE)
