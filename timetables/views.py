from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Timetable
from rest_framework import routers, serializers, viewsets
from .serializers import TimetableSerializer
# orm


class TimetableViewSet(viewsets.ModelViewSet):
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer


