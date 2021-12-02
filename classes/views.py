from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Classe
from rest_framework import routers, serializers, viewsets
from .serializers import ClasseSerializer
# orm


class ClasseViewSet(viewsets.ModelViewSet):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer
    filter_fields = ('name',)
