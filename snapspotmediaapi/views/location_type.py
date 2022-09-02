from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from snapspotmediaapi.models import LocationPost, Location, LocationType
from snapspotmediaapi.models.driver import Driver


class LocationTypeView(ViewSet):

    def retrieve(self, request, pk):
        location_types = LocationType.objects.get(pk=pk)
        serializer = LocationTypeSerializer(location_types)
        return Response(serializer.data)

    def list(self, request):
        location_types = LocationType.objects.all()
        serializer = LocationTypeSerializer(location_types, many=True)
        return Response(serializer.data)
    
class LocationTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = LocationType
        fields = ('id', 'locationId', 'location_type')