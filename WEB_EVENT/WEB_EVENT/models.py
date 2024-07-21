# models of the WEB_EVENT project

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    login = models.CharField(max_length=30)
    age = models.IntegerField()
    role = models.CharField()
    password = models.CharField(max_length=30)


class Organizer(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    login = models.CharField(max_length=30)
    age = models.IntegerField()
    role = models.CharField()
    password = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    # ToDo events_list = ?


class Event(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField()
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
