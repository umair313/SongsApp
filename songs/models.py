from unicodedata import name
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=20)

class Album(models.Model):
    name = models.CharField(max_length=100)
    album_artist = models.ForeignKey(Artist, related_name='artist')

class Genre(models.Model):
    name = models.CharField(max_length=10)

class Playlist(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(get_user_model(), related_name='user')