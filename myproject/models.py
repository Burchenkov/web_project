#Узнать про токен пользователя и как его написать
from django.db import models



class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    
    
    
class CategoryEvent(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length = 50)

    def __str__(self):
        return self.name
    
    

# Create your models here.
