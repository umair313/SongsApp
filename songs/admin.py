from django.contrib import admin
from .models import Artist, Track, Genre, Playlist, Album, PlaylistTrack
# Register your models here.

admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Playlist)
admin.site.register(Album)
admin.site.register(PlaylistTrack)

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
