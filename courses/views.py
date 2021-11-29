from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Course
from rest_framework import routers, serializers, viewsets
from .serializers import CourseSerializer
# orm


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


