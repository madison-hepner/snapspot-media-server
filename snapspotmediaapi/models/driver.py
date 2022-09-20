from django.db import models
from django.contrib.auth.models import User
from .location import Location
from .permission import Permission


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    permissions = models.ManyToManyField("Permission", through="DriverPermissions", related_name="the_driver_permissions")
