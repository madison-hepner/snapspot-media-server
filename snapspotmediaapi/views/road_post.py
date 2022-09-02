"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from snapspotmediaapi.models import RoadPost
from snapspotmediaapi.models.driver import Driver


class RoadPostView(ViewSet):

    def retrieve(self, request, pk):
        road_posts = RoadPost.objects.get(pk=pk)
        serializer = RoadPostSerializer(road_posts)
        return Response(serializer.data)

    def list(self, request):
        road_posts = RoadPost.objects.all()
        serializer = RoadPostSerializer(road_posts, many=True)
        return Response(serializer.data)


class RoadPostSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = RoadPost
        fields = ('id', 'road_name', 'description', 'locationImg',
                  'driver', 'locationId', 'road_type')