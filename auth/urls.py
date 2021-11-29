from django.urls import path, include
# from .views import ExampleAuthentication
from .views import *
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('api', ExampleAuthentication)


urlpatterns = [
    path('', login_view),

]
