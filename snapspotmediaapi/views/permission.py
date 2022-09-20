from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from snapspotmediaapi.models import DriverPermissions, Driver, Permission



class PermissionView(ViewSet):

    def retrieve(self, request, pk):
        permissions = Permission.objects.get(pk=pk)
        serializer = PermissionSerializer(permissions)
        return Response(serializer.data)

    def list(self, request):
        permissions = Permission.objects.all()
        serializer = PermissionSerializer(permissions, many=True)
        return Response(serializer.data)

    
class PermissionSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Permission
        fields = ('id', 'permission')