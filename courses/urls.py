from django.urls import path, include
from .views import CourseViewSet, DownloadCourse
# from courses.views import  *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('courses-api', CourseViewSet)


urlpatterns = [
    path('', include(router.urls)),

]
