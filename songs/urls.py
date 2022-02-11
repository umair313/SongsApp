from django.urls import path
from .views import (ListView, ArtistListView, AlbumListView, LikeSongsPlaylistView,
                    PlaylistView,PlaylistDeleteView,TrackDetailView, AlbumDetailView, 
                    ArtistDetailView, createPlaylist, addTrackToPlaylist,
                    removeTrackFromPlaylist,LikeTrack, UnlikeTrack, homeView)
urlpatterns = [
    path('', homeView, name='home'),
    path('list/', ListView.as_view(), name='listing'),
    path('artists/', ArtistListView.as_view(), name='artist_list'),
    path('albums/', AlbumListView.as_view(), name='album_list'),
    path('track/<slug:slug>/', TrackDetailView.as_view(), name='track_view'),
    path('artist/<int:pk>/', ArtistDetailView.as_view(), name='artist_view'),
    path('album/<int:pk>/', AlbumDetailView.as_view(), name='album_view'),

    path("track/like/<int:track_id>/", LikeTrack, name='track_like'),
    path("track/unlike/<int:track_id>/", UnlikeTrack, name='track_unlike'),

    path('playlist/default/', LikeSongsPlaylistView.as_view(), name='playlist_default'),
    path('playlist/create/<str:name>/', createPlaylist, name="playlist_create"),
    path('playlist/<int:pk>/', PlaylistView.as_view(), name='playlist_view'),
    path('playlist/delete/<int:pk>/', PlaylistDeleteView.as_view(), name='playlist_delete_view'),
    path('playlist/<int:playlist_id>/add/track/<int:track_id>/', addTrackToPlaylist, name='playlist_add_track'),
    path('playlist/<int:playlist_id>/remove/track/<int:track_id>/', removeTrackFromPlaylist, name='playlist_add_track'),
]
