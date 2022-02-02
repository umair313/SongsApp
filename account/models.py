from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    following = models.ManyToManyField('songs.Artist')

    def __str__(self):
        return self.username
