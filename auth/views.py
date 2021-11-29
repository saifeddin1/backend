from json.encoder import JSONEncoder
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from rest_framework import authentication
from rest_framework import exceptions


def login_view(request):
    body = request.body
    print(body)
    user = User.objects.get(username=body.username, password=body.password)

    if user is not None:
        request.user = user
        return JsonResponse({"username": user.username})
    else:
        return JsonResponse({'res': 'none'})

# class ExampleAuthentication(authentication.BaseAuthentication):
#     def authenticate(self, request):
#         username = request.META.get('HTTP_X_USERNAME')
#         password = request.META.get('HTTP_X_PASSWORD')
#         if not username:
#             return None

#         try:
#             user = User.objects.get(username=username)
#         except User.DoesNotExist:
#             raise exceptions.AuthenticationFailed('No such user')

#         return (user, None)
