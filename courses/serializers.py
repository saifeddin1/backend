from rest_framework import routers, serializers, viewsets
from .models import Course

# Serializers define the API representation.


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    course_classe = serializers.ReadOnlyField(source='classe.name')

    class Meta:
        model = Course
        fields = ['id', 'title', 'content', 'classe', 'course_classe']
