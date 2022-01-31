from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=100)
    album_artist = models.ForeignKey(Artist, related_name='album_artist', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Playlist(models.Model):
    name = models.CharField(max_length=50, default='Liked Songs')
    user = models.ForeignKey(get_user_model(), related_name='playlist_user', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


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


class PlaylistTrack(models.Model):
    playlist = models.ForeignKey(Playlist, related_name='playlist_playlist', on_delete=models.CASCADE)
    track = models.ForeignKey(Track, related_name='playlist_track', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.playlist.name}"
        