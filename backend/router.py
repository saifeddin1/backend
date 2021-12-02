from rest_framework import routers
from profiles.views import ProfileViewSet
from courses.views import CourseViewSet
from classes.views import ClasseViewSet
from timetables.views import TimetableViewSet

router = routers.DefaultRouter()
router.register('profiles', ProfileViewSet)
router.register('classes', ClasseViewSet)
router.register('courses', CourseViewSet)
router.register('timetables', TimetableViewSet)
