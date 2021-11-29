from django.urls import path, include
from .views import TimetableViewSet
# from Timetables.views import  *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('timetables-api', TimetableViewSet)


urlpatterns = [
    path('', include(router.urls)),

]
    