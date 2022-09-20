"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from snapspotmediaapi.models import Driver


class DriverView(ViewSet):

    def retrieve(self, request, pk):
        drivers = Driver.objects.get(pk=pk)
        serializer = DriverSerializer(drivers)
        return Response(serializer.data)

    def list(self, request):
        drivers = Driver.objects.all()
        serializer = DriverSerializer(drivers, many=True)
        return Response(serializer.data)
    
    


class DriverSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Driver
        fields = ('id', 'user', 'permissions')
