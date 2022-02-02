from csv import list_dialects
from django.contrib import admin
from .models import (Artist, Track, Genre,
                     Playlist, Album, PlaylistTrack)

# Register your models here.

admin.site.register(PlaylistTrack)


@admin.register(Playlist, Album, Artist, Genre)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    prepopulated_fields = {'slug': ('title',)}
