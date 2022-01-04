from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
# from courses.views import  *
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
from django.contrib.auth.views import LoginView, LogoutView
from .router import router
from courses.views import DownloadCourse
from timetables.views import DownloadTimetable

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('courses/', include('courses.urls')),
    # path('classes/', include('classes.urls')),
    # path('profiles/', include('profiles.urls')),
    # path('timetables/', include('timetables.urls')),
    path('api/', include(router.urls)),
    path('file_uploads/courses/<filename>',
         DownloadCourse, name='download_course'),
    path('file_uploads/timetables/<filename>',
         DownloadTimetable, name='download_timetable'),

    path('api-token-auth/', obtain_auth_token,
         name='api_token_auth'),  # <-- And here
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),

]
