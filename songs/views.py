from django.shortcuts import render
from django.views.generic import ListView, FormView
from .forms import SearchForm
from .models import Genre, Album, Track, Artist
# Create your views here.


class ListingView(ListView):

    model = Track
    template_name = 'search/lists.html'
    context_object_name = 'result'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            tracks = Track.objects.filter(title__icontains=query)
            albums = Album.objects.filter(name__icontains=query)
            artists = Artist.objects.filter(name__icontains=query)
            self.context_object_name = 'q'
            return {
                'tracks': tracks,
                'albums': albums,
                'artists': artists
            }

        return Track.objects.all()[:10]


class ArtistListView(ListView):
    model = Artist
    template_name = 'app/artistlisting.html'


class AlbumListView(ListView):
    model = Album
    template_name = 'app/albumslisting.html'


