from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
# Create your views here.
from .models import Timetable
from rest_framework import routers, serializers, viewsets
from .serializers import TimetableSerializer
from backend.settings import BASE_DIR, MEDIA_ROOT
from django.core.files import File


@api_view(['GET'])
def DownloadTimetable(request, filename):
    path_to_file = MEDIA_ROOT + f'timetables/{filename}'
    print("\n", path_to_file)
    f = open(path_to_file, 'rb')
    pdfFile = File(f)
    response = HttpResponse(pdfFile.read())
    response['Content-Type'] = 'application/pdf'
    return response


class TimetableViewSet(viewsets.ModelViewSet):
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer
