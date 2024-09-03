from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, date, time
from django.conf import settings


from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
import jwt
from datetime import datetime, timedelta

from .models import User, Event, Comment
from .serializers import UserSerializer, EventSerializer, UserLoginSerializer, CommentSerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def user_create(request):   # signup(creation) procedure of new user
    user_data = JSONParser().parse(request)
    user_serializer = UserSerializer(data=user_data)
    if user_serializer.is_valid():
        user_serializer.save()
        return JSONResponse(user_serializer.data, status=status.HTTP_201_CREATED)
    return JSONResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def users_get(request):  # getting of all users objects
    if request.method == 'GET':
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return JSONResponse(users_serializer.data, status=status.HTTP_200_OK)


@csrf_exempt
def user_login(request):  # signin procedure with checking login & password
    credentials_data = JSONParser().parse(request)
    user_serializer = UserLoginSerializer(credentials_data)
    input_login = user_serializer.data["login"]  # login which input by user
    input_password = user_serializer.data["password"]  # password which input by user

    try:
        db_user_object = User.objects.get(login=input_login)  # getting user object from db & checking that is exists
    except ObjectDoesNotExist:
        content = "Login does not exist. Please SingUP at first"
        return HttpResponse(content, status=status.HTTP_401_UNAUTHORIZED)

    if input_password == db_user_object.password:  # checking password if the user exists
        pk = db_user_object.id
        token = _generate_jwt_token(request, pk)
        return JSONResponse(token, status=status.HTTP_200_OK)
    else:
        content = "The password is incorrect"
        return HttpResponse(content, status=status.HTTP_401_UNAUTHORIZED)


def _generate_jwt_token(request, pk):
    """
    Генерирует WEBтокен JSON, в котором хранится id пользователя, срок действия токена
    60 дней с момента создания
    """
    dt = datetime.now() + timedelta(days=60)

    token = jwt.encode({
        'id': pk,
        'exp': int(dt.timestamp())
    }, settings.SECRET_KEY, algorithm='HS256')

    return token


@csrf_exempt
def user_change(request, pk):  # update & delete user by pk(id). For that we need pk.
    try:
        user_obj = User.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # get the certain USER by pk
    if request.method == 'GET':
        user_serializer = UserSerializer(user_obj)
        return JSONResponse(user_serializer.data)

    # update USER object
    if request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(user_obj, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JSONResponse(user_serializer.data, status=status.HTTP_200_OK)
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    # delete USER object
    if request.method == 'DELETE':
        user_obj.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def events_get(request):  # getting of all events objects
    if request.method == 'GET':
        events = Event.objects.all()
        events_serializer = EventSerializer(events, many=True)
        return JSONResponse(events_serializer.data, status=status.HTTP_200_OK)


@csrf_exempt
def event_add(request):  # add a new event object
    event_data = JSONParser().parse(request)
    event_serializer = EventSerializer(data=event_data)
    if event_serializer.is_valid():
        event_serializer.save()
        return JSONResponse(event_serializer.data, status=status.HTTP_201_CREATED)
    return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def event_change(request, pk):  # update of certain event object
    try:
        event_obj = Event.objects.get(pk=pk)  # get of certain event object from DB by pk
    except ObjectDoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # get the certain event by pk
    if request.method == 'GET':
        event_serializer = EventSerializer(event_obj)
        return JSONResponse(event_serializer.data)

    # update event object
    if request.method == 'PUT':
        event_data = JSONParser().parse(request)
        event_serializer = EventSerializer(event_obj, data=event_data)
        if event_serializer.is_valid():
            event_serializer.save()
            return JSONResponse(event_serializer.data, status=status.HTTP_200_OK)
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    # delete event object
    if request.method == 'DELETE':
        event_obj.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def comment_add(request):
    if request.method == 'POST':
        comment_data = JSONParser().parse(request)
        comment_serializer = CommentSerializer(comment_data)
        comment_text = comment_serializer.data['text']
        timestamp = datetime.now()
        comment_obj = Comment(text=comment_text, created_at=timestamp)
        comment_obj.save()
    return HttpResponse(status=status.HTTP_201_CREATED)


@csrf_exempt
def comment_delete(request):
    comment_data = JSONParser().parse(request)
    pk = comment_data['pk']
    print(f'pk = {pk}')
    comment_obj = Comment.objects.get(pk=pk)
    comment_obj.delete()
    return HttpResponse(status=status.HTTP_204_NO_CONTENT)
