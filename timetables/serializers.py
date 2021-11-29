from rest_framework import routers, serializers, viewsets
from .models import Timetable

# Serializers define the API representation.
class TimetableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Timetable
        fields = '__all__'

        

