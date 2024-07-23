from . models import User, Organizer, Event
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    email = serializers.CharField(max_length=100)
    login = serializers.CharField(max_length=30)
    role = serializers.CharField(default='user')
    password = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return User.objects.create(**validated_data)


class EventSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    category = serializers.CharField()
    date = serializers.DateTimeField()
    location = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=1024)

    def create(self, validated_data):
        return Event.objects.create(**validated_data)
