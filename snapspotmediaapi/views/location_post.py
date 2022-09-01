"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from snapspotmediaapi.models import LocationPost, Location, LocationType
from snapspotmediaapi.models.driver import Driver


class LocationPostView(ViewSet):

    def retrieve(self, request, pk):
        location_posts = LocationPost.objects.get(pk=pk)
        serializer = LocationPostSerializer(location_posts)
        return Response(serializer.data)

    def list(self, request):
        location_posts = LocationPost.objects.all()
        serializer = LocationPostSerializer(location_posts, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized game instance
        """
        driver = Driver.objects.get(user=request.auth.user)
        serializer = CreateLocationPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(driver=driver)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """

        location_post = LocationPost.objects.get(pk=pk)
        location_post.title = request.data["title"]
        location_post.description = request.data["description"]
        location_post.locationImg = request.data["locationImg"]
        location_post.locationId = request.data["locationId"]

        location_type = LocationType.objects.get(
            pk=request.data["location_type"])
        location_post.location_type = location_type
        location_post.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class CreateLocationPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationPost
        fields = ['id', 'title', 'description', 'locationImg',
                  'driver', 'locationId', 'location_type']


class LocationPostSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = LocationPost
        fields = ('id', 'title', 'description', 'locationImg',
                  'driver', 'locationId', 'location_type')
