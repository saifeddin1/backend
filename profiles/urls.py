from django.urls import path, include
from .views import ProfileViewSet
# from Profiles.views import  *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('profiles-api', ProfileViewSet)


urlpatterns = [
    path('', include(router.urls)),

]
    