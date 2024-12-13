from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    phone=models.CharField(max_length=20,unique=True)

class Todo(models.Model):

    title=models.CharField(max_length=200)

    create_date=models.DateTimeField(auto_now=True)

    status=models.BooleanField(default=False)

    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
