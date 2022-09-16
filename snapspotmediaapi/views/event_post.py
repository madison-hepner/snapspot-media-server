"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from snapspotmediaapi.models import EventPost, Location, LocationType
from snapspotmediaapi.models.driver import Driver
from datetime import datetime


class EventPostView(ViewSet):

    def retrieve(self, request, pk):
        event_posts = EventPost.objects.get(pk=pk)
        serializer = EventPostSerializer(event_posts)
        return Response(serializer.data)

    def list(self, request):
        event_posts = EventPost.objects.all()
        serializer = EventPostSerializer(event_posts, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        driver = Driver.objects.get(user=request.auth.user)
        location_type = LocationType.objects.get(
            pk=request.data["location_type"])
        locationId = Location.objects.get(pk=request.data["locationId"])
        date_string = request.data["date"]
        # date_time = datetime.striptime(date_string, "%Y-%m-%d")
        # date_time = datetime.strftime(date_string, '%Y-%m-%d %H:%M')
        event_post = EventPost.objects.create(
            event_name=request.data["event_name"],
            description=request.data["description"],
            driver=driver,
            location_type=location_type,
            locationId=locationId,
            date=date_string
        )
        serializer = EventPostSerializer(event_post)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """

        event_post = EventPost.objects.get(pk=pk)
        event_post.event_name = request.data["event_name"]
        event_post.description = request.data["description"]
        event_post.date = request.data["date"]

        location_type = LocationType.objects.get(
            pk=request.data["location_type"])
        event_post.location_type = location_type

        locationId = Location.objects.get(
            pk=request.data["locationId"])
        event_post.locationId = locationId

        event_post.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        event_post = EventPost.objects.get(pk=pk)
        event_post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


# class CreateLocationPostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LocationPost
#         fields = ['id', 'title', 'description',
#                   'locationImg', 'locationId', 'location_type']


class EventPostSerializer(serializers.ModelSerializer):
    """JSON serializer for event posts
    """
    class Meta:
        model = EventPost
        fields = ('id', 'event_name', 'description', 'driver',
                  'locationId', 'location_type', 'date')
        depth = 1
