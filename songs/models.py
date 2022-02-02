from django_extensions.db.models import TimeStampedModel 
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Artist(TimeStampedModel, models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Album(TimeStampedModel, models.Model):
    name = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='thumbnails')
    artist = models.ForeignKey('Artist', related_name='albums', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Genre(TimeStampedModel, models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Playlist(TimeStampedModel, models.Model):
    name = models.CharField(max_length=50, default='Liked Songs')
    owner = models.ForeignKey(get_user_model(), related_name='playlists', on_delete=models.CASCADE)
    tracks = models.ManyToManyField('Track', through='PlaylistTrack')

    def __str__(self):
        return self.name


class Track(TimeStampedModel, models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    audio_file = models.FileField(upload_to='tracks')
    artist = models.ForeignKey('Artist', related_name='tracks', on_delete=models.CASCADE)
    album = models.ForeignKey('Album', related_name='tracks', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', related_name='tracks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class PlaylistTrack(models.Model):
    playlist = models.ForeignKey('Playlist', related_name='playlists', on_delete=models.CASCADE)
    track = models.ForeignKey('Track', related_name='tracks', on_delete=models.CASCADE)

    def __str__(self):
        return f"({self.playlist.name}, {self.track.title})"
