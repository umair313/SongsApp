from distutils.command.upload import upload
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

class Track(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    thumbnails = models.ImageField(upload_to='thumbnails')
    artist = models.ForeignKey(Artist, related_name='artist')
    album = models.ForeignKey(Album, related_name='album')
    genre = models.ForeignKey(Genre, related_name='genre')

    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.title
