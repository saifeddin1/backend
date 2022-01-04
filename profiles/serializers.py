from rest_framework import routers, serializers, viewsets
from .models import Profile

# Serializers define the API representation.


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    profile_classe = serializers.ReadOnlyField(source='classe.name')

    class Meta:
        model = Profile
        fields = ('id', 'first_name', 'last_name', 'cin',
                  'birthdate', 'email', 'classe', 'role', 'username', 'profile_classe')
