from rest_framework import routers, serializers, viewsets
from .models import Classe

# Serializers define the API representation.
class ClasseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Classe
        fields = ['id', 'name']



        

