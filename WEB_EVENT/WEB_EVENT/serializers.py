from . models import User, Admin, Organizer, Event
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = {
            'pk',
            'email',
            'login',
            'role',
            'password',
            'secret_phrase',
            'avatar',
        }


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = {
            'pk',
            'email',
            'login',
            'role',
            'password',
            'secret_phrase',
            'avatar',
        }


class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        fields = {
            'pk',
            'email',
            'login',
            'role',
            'password',
            'secret_phrase',
            'avatar',
        }


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = {
            'pk',
            'event_name',
            'city',
            'description',
            'price',
            'image',
            'age_limit',
            'start_time',
            'duration',
            'user_limit',
        }
