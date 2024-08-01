from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import User, Event
from .serializers import UserSerializer, EventSerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def user_create(request):
    user_data = JSONParser().parse(request)
    user_serializer = UserSerializer(data=user_data)
    if request.method == 'POST':
        if user_serializer.is_valid():
            user_serializer.save()
            return JSONResponse(user_serializer.data, status=status.HTTP_201_CREATED)
    return JSONResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def user_login(request):
    credentials_data = JSONParser().parse(request)
    user_serializer = UserSerializer(credentials_data)
    input_login = user_serializer.data["login"]         # login which input by user
    input_password = user_serializer.data["password"]   # password which input by user
    print(f"Login: {input_login}")
    print(f"Password: {input_password}")

    return JSONResponse(user_serializer.data["login"], status=status.HTTP_200_OK)


@csrf_exempt
def events_get(request):
    events = Event.objects.all()
    events_serializer = EventSerializer(events, many=True)
    return JSONResponse(events_serializer.data, status=status.HTTP_200_OK)

