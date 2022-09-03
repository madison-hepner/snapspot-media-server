"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from snapspotmediaapi.models import RoadType
from snapspotmediaapi.models.driver import Driver


class RoadTypeView(ViewSet):

    def retrieve(self, request, pk):
        road_types = RoadType.objects.get(pk=pk)
        serializer = RoadTypeSerializer(road_types)
        return Response(serializer.data)

    def list(self, request):
        road_types = RoadType.objects.all()
        serializer = RoadTypeSerializer(road_types, many=True)
        return Response(serializer.data)


class RoadTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = RoadType
        fields = ('id', 'road_type')
