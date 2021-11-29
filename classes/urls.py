from django.urls import path, include
from .views import ClasseViewSet
# from courses.views import  *
from rest_framework import routers


router = routers.DefaultRouter()
router.register('classes-api', ClasseViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
    