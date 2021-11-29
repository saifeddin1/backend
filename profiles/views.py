from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Profile
from rest_framework import routers, serializers, viewsets
from .serializers import ProfileSerializer
# orm


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


