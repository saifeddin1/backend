from django.urls import path
from .views import home 
# from courses.views import  *


urlpatterns = [
    path('', home),
]
