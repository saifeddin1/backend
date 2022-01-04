from rest_framework import routers, serializers, viewsets
from .models import Timetable


class TimetableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Timetable
        fields = ['id', 'content', 'classe']
