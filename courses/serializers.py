from rest_framework import routers, serializers, viewsets
from .models import Course

# Serializers define the API representation.
class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['title', 'content']

        

