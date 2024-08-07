# models of the WEB_EVENT project

from django.db import models
from datetime import datetime


class User(models.Model):
    email = models.CharField(max_length=100, unique=True)
    login = models.CharField(max_length=30, unique=True)
    role = models.CharField(max_length=30, default="user")
    password = models.CharField(max_length=30)
    secret_phrase = models.CharField(max_length=30)
    avatar = models.CharField(max_length=100)

    objects = models.Manager()

    class Meta:
        ordering = ('email',)


class Admin(User):

    objects = models.Manager()

    class Meta:

        ordering = ('email',)


class Organizer(User):

    objects = models.Manager()

    class Meta:
        ordering = ('email',)


class Event(models.Model):
    event_name = models.CharField(max_length=200)
    date = models.DateField(default=datetime.now)
    city = models.CharField(default='', max_length=50)
    description = models.CharField(max_length=1024)
    price = models.IntegerField(default=0)
    image = models.CharField(max_length=100)
    age_limit = models.IntegerField(default=0)
    start_time = models.TimeField(null=True)
    duration = models.IntegerField(default=0)
    user_limit = models.IntegerField(default=0)

    objects = models.Manager()

    class Meta:
        ordering = ('event_name',)


class Comment(models.Model):
    text = models.TextField(max_length=1024)
    created_at = models.DateTimeField()

    objects = models.Manager()
