from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    # custom user model to add extra fields
    following = models.ManyToManyField('songs.Artist')

    def __str__(self):
        return self.username
