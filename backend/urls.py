from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
# from courses.views import  *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),
    path('classes/', include('classes.urls')),
    path('profiles/', include('profiles.urls')),
    path('timetables/', include('timetables.urls')),
    path('auth/', include('auth.urls')),


]
