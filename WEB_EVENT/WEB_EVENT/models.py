# models of the WEB_EVENT project

from django.db import models
from datetime import datetime


class User(models.Model):
    email = models.CharField(max_length=100)
    login = models.CharField(max_length=30)
    role = models.CharField(default="user")
    password = models.CharField(max_length=30)

    objects = models.Manager()

    class Meta:
        ordering = ('email', )


class Organizer(models.Model):
    email = models.CharField(max_length=100)
    login = models.CharField(max_length=30)
    role = models.CharField()
    password = models.CharField(max_length=30)

    objects = models.Manager()

    class Meta:
        ordering = ('email', )


class Event(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField()
    date = models.DateTimeField(default=datetime.now)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=1024)

    objects = models.Manager()

    class Meta:
        ordering = ('title',)
