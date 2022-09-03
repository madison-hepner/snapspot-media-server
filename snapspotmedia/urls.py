from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from snapspotmediaapi.views import register_user, login_user
from snapspotmediaapi.views import LocationView
from snapspotmediaapi.views.location_post import LocationPostView
from snapspotmediaapi.views.location_type import LocationTypeView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'locations', LocationView, 'location')
router.register(r'location_posts', LocationPostView, 'location_post')
router.register(r'location_types', LocationTypeView, 'location_type')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

]
