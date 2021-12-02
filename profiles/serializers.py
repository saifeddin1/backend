from rest_framework import routers, serializers, viewsets
from .models import Profile

# Serializers define the API representation.


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'cin',
                  'birthdate', 'email', 'classe')
