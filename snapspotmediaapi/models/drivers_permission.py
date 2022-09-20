from django.db import models
from django.contrib.auth.models import User
from .driver import Driver
from .permission import Permission



class DriverPermissions(models.Model):
    permissionId = models.ForeignKey(Permission, on_delete=models.CASCADE)
    userId = models.ForeignKey(Driver, on_delete=models.CASCADE)
    
