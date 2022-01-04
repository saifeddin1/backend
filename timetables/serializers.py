from rest_framework import routers, serializers, viewsets
from .models import Timetable


class TimetableSerializer(serializers.HyperlinkedModelSerializer):
    timetable_classe = serializers.ReadOnlyField(source='classe.name')

    class Meta:
        model = Timetable
        fields = ['id', 'content', 'classe', 'timetable_classe']
