from django.db import models


class RoadType(models.Model):
    road_type = models.CharField(max_length=55)
