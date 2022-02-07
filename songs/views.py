from re import template
from django.shortcuts import render
from django.views import generic as generic_views
from .models import Album, Track, Artist, Playlist
# Create your views here.


class ListView(generic_views.View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        if query:
            context = {
                "tracks": Track.objects.filter(title__icontains=query),
                "artists": Artist.objects.filter(name__icontains=query),
                "albums": Album.objects.filter(name__icontains=query)
            }
            return render(request, 'app/lists.html', context=context)

        tracks = Track.objects.all()[:10]

        return render(request, 'app/lists.html', context={"trackslist": tracks})


class ArtistListView(generic_views.ListView):
    model = Artist
    template_name = 'app/artistlisting.html'


class AlbumListView(generic_views.ListView):
    model = Album
    template_name = 'app/albumslisting.html'


class TrackDetailView(generic_views.DetailView):
    model = Track
    template_name = 'app/track.html'

class AlbumDetailView(generic_views.DetailView):
    model = Album
    template_name = 'app/album.html'


class PlaylistDetailView(generic_views.DetailView):
    model = Playlist
    template_name = 'app/playlist.html'

class ArtistDetailView(generic_views.DeleteView):
    model = Artist
    template_name = 'app/artist.html'

