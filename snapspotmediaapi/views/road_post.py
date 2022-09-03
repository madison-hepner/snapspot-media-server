"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from snapspotmediaapi.models import RoadPost
from snapspotmediaapi.models import Driver
from snapspotmediaapi.models import RoadType
from snapspotmediaapi.models.location import Location


class RoadPostView(ViewSet):

    def retrieve(self, request, pk):
        road_posts = RoadPost.objects.get(pk=pk)
        serializer = RoadPostSerializer(road_posts)
        return Response(serializer.data)

    def list(self, request):
        road_posts = RoadPost.objects.all()
        serializer = RoadPostSerializer(road_posts, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        driver = Driver.objects.get(user=request.auth.user)
        road_type = RoadType.objects.get(pk=request.data["road_type"])
        locationId = Location.objects.get(pk=request.data["locationId"])

        road_post = RoadPost.objects.create(
            road_name=request.data["road_name"],
            description=request.data["description"],
            locationImg=request.data["locationImg"],
            driver=driver,
            locationId=locationId,
            road_type=road_type
        )
        serializer = RoadPostSerializer(road_post)
        return Response(serializer.data)


class RoadPostSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = RoadPost
        fields = ('id', 'road_name', 'description', 'locationImg',
                  'driver', 'locationId', 'road_type')