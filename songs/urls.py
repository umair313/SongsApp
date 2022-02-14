from django.urls import path
from .views import (ListView, ArtistListView, AlbumListView, LikeSongsPlaylistView,
                    PlaylistView,PlaylistDeleteView, TrackDetailView, AlbumDetailView,
                    ArtistDetailView, create_playlist, add_track_to_playlist,
                    remove_track_from_playlist, like_track, unlike_track, homeView)
urlpatterns = [
    path('', homeView, name='home'),
    path('list/', ListView.as_view(), name='listing'),
    path('artists/', ArtistListView.as_view(), name='artist_list'),
    path('albums/', AlbumListView.as_view(), name='album_list'),
    path('track/<slug:slug>/', TrackDetailView.as_view(), name='track_view'),
    path('artist/<int:pk>/', ArtistDetailView.as_view(), name='artist_view'),
    path('album/<int:pk>/', AlbumDetailView.as_view(), name='album_view'),

    path("track/like/<int:track_id>/", like_track, name='track_like'),
    path("track/unlike/<int:track_id>/", unlike_track, name='track_unlike'),

    path('playlist/default/', LikeSongsPlaylistView.as_view(), name='playlist_default'),
    path('playlist/create/<str:name>/', create_playlist, name="playlist_create"),
    path('playlist/<int:pk>/', PlaylistView.as_view(), name='playlist_view'),
    path('playlist/delete/<int:pk>/', PlaylistDeleteView.as_view(), name='playlist_delete_view'),
    path('playlist/<int:playlist_id>/add/track/<int:track_id>/', add_track_to_playlist, name='playlist_add_track'),
    path('playlist/<int:playlist_id>/remove/track/<int:track_id>/', remove_track_from_playlist, name='playlist_add_track'),
]
