from django.urls import path
from .views import ListingView, ArtistListView, AlbumListView
urlpatterns = [
    path('listing/', ListingView.as_view(), name='listing'),
    path('listing/artists/', ArtistListView.as_view(), name='artist_list'),
    path('listing/albums/', AlbumListView.as_view(), name='album_list')
]
