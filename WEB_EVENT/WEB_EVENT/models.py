# models of the WEB_EVENT project

from django.db import models
from django.conf import settings

import jwt
from datetime import datetime, timedelta


class User(models.Model):
    email = models.CharField(max_length=100, unique=True)
    login = models.CharField(max_length=30, unique=True)
    role = models.CharField(default="user")
    password = models.CharField(max_length=30)
    secret_phrase = models.CharField(max_length=30)
    avatar = models.CharField(max_length=100)

    # свойство USERNAME_FIELD сообщает нам, какое поле мы будем использовать
    # для входа в систему. В данном случаем мы будем использовать логин
    USERNAME_FIELD = 'login'

    objects = models.Manager()

    class Meta:
        ordering = ('email',)

    @property
    def token(self):
        """
            Позволяет получить token пользователя путем вызова user.token, вместо
            user._generate_jwt_token. Декоратор @property делает это возможным.
        """
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        """
        Генерирует WEBтокен JSON, в котором хранится id пользователя, срок действия токена
        60 дней с момента создания
        """
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.timestamp())
        }, settings.SECRET_KEY, algorithm='HS256')

        return token


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
        ordering = ('pk',)


class Comment(models.Model):
    text = models.TextField(max_length=1024)
    created_at = models.DateTimeField()

    objects = models.Manager()
