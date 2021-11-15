from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from courses.views import home 
# from courses.views import  *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),

]
