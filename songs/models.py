from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=20)

class Album(models.Model):
    name = models.CharField(max_length=100)
    album_artist = models.ForeignKey(Artist, related_name='album_artist', on_delete=models.CASCADE)

class Genre(models.Model):
    name = models.CharField(max_length=10)

class Playlist(models.Model):
    name = models.CharField(max_length=20, default='Liked Songs')
    user = models.ForeignKey(get_user_model(), related_name='playlist_user', on_delete=models.CASCADE)

class Track(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    thumbnails = models.ImageField(upload_to='thumbnails')
    artist = models.ForeignKey(Artist, related_name='track_artist', on_delete=models.CASCADE)
    album = models.ForeignKey(Album, related_name='track_album', on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, related_name='track_genre', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.title
