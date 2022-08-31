from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from snapspotmediaapi.views import register_user, login_user
from snapspotmediaapi.views import LocationView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'locations', LocationView, 'location')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

]
