from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Profile
from rest_framework import routers, serializers, viewsets
from .serializers import ProfileSerializer
from django_filters import rest_framework as filters
# orm


class ProfileFilter(filters.FilterSet):

    class Meta:
        model = Profile
        fields = {
            'first_name': ['icontains'],
            'birthdate': ['iexact', 'lte', 'gte']
        }


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filterset_class = ProfileFilter
