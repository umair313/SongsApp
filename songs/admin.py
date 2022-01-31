from csv import list_dialects
from django.contrib import admin
from .models import (Artist, Track, Genre,
                    Playlist, Album, PlaylistTrack)

# Register your models here.

admin.site.register(PlaylistTrack)

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'created')

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created')

@admin.register(Artist, Genre)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name','created')

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist','album','genre', 'created')
    prepopulated_fields = {'slug':('title',)}
