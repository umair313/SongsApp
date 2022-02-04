from django.urls import path
from .views import ListView, ArtistListView, AlbumListView
urlpatterns = [
    path('list/', ListView.as_view(), name='listing'),
    path('listing/artists/', ArtistListView.as_view(), name='artist_list'),
    path('listing/albums/', AlbumListView.as_view(), name='album_list')
]
