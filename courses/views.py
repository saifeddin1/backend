from django.db import reset_queries
from django.shortcuts import render
from django.http import HttpResponse, request
from rest_framework.response import Response
# Create your views here.
from .models import Course
from rest_framework.permissions import IsAuthenticated

from rest_framework import routers, serializers, viewsets, status
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from .serializers import CourseSerializer
# orm
import json
from django.core.files import File
from django.http import HttpResponse
from rest_framework.decorators import api_view
from backend.settings import BASE_DIR, MEDIA_ROOT


@api_view(['GET'])
def DownloadCourse(request, filename):
    path_to_file = MEDIA_ROOT + f'courses/{filename}'
    print("\n", path_to_file)
    f = open(path_to_file, 'rb')
    pdfFile = File(f)
    response = HttpResponse(pdfFile.read())
    response['Content-Type'] = 'application/pdf'
    return response


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    # permission_classes = [IsAuthenticated]
    parser_class = [MultiPartParser]

    serializer_class = CourseSerializer

    def create(self, request, *args, **kwargs):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            print('im valid')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
