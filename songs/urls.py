from django.urls import path
from .views import ListView, ArtistListView, AlbumListView, TrackDetailView, PlaylistDetailView, AlbumDetailView, ArtistDetailView
urlpatterns = [
    path('list/', ListView.as_view(), name='listing'),
    path('listing/artists/', ArtistListView.as_view(), name='artist_list'),
    path('listing/albums/', AlbumListView.as_view(), name='album_list'),
    path('track/<slug:slug>/', TrackDetailView.as_view(), name='track_view'),
    path('playlist/<int:pk>/', PlaylistDetailView.as_view(), name='playlist_view'),
    path('artist/<int:pk>/', ArtistDetailView.as_view(), name='artist_view'),
    path('album/<int:pk>/', AlbumDetailView.as_view(), name='album_view')
]
