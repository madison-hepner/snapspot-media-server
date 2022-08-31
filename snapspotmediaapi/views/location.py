"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from snapspotmediaapi.models import Location


class LocationView(ViewSet):

    def retrieve(self, request, pk):
        locations = Location.objects.get(pk=pk)
        serializer = LocationSerializer(locations)
        return Response(serializer.data)

    def list(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)


class LocationSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Location
        fields = ('id', 'locationName')
