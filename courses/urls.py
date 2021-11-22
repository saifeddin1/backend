from django.urls import path, include
from .views import home , CourseViewSet
# from courses.views import  *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('courses', CourseViewSet)


urlpatterns = [
    path('', home),
    path('api', include(router.urls)),

]
    