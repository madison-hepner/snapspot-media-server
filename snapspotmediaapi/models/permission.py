from django.db import models
from django.contrib.auth.models import User


class Permission(models.Model):
    permission = models.CharField(max_length=55)
    
