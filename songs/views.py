from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
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
    context_object_name = 'track'
    template_name = 'app/track.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["liked_tracks"] = user.playlists.filter(name="Liked Songs").first().tracks.all()
        return context


class AlbumDetailView(generic_views.DetailView):
    model = Album
    context_object_name = 'album'
    template_name = 'app/album.html'


class ArtistDetailView(generic_views.DeleteView):
    model = Artist
    context_object_name = 'artist'
    template_name = 'app/artist.html'


class LikeSongsPlaylistView(generic_views.View):
    def get(self, request, *args, **kwargs):
        user = request.user
        playlist = Playlist.objects.get(name='Liked Songs', owner=user)
        tracks = playlist.tracks.all()
        return render(request, 'app/playlist.html', context={"tracks": tracks})


def LikeTrack(request, track_id):
    user = request.user
    playlist = Playlist.objects.get(name='Liked Songs', owner=user)
    track = get_object_or_404(Track, id=track_id)
    if track:
        playlist.tracks.add(track)
        return JsonResponse({'message': True})
    else:
        return JsonResponse({'message': False})
        

def UnlikeTrack(request, track_id):
    user = request.user
    playlist = Playlist.objects.get(name='Liked Songs', owner=user)
    tracks = playlist.tracks.all()
    track = get_object_or_404(Track, id=track_id)
    if track in tracks :
        playlist.tracks.remove(track)
        return JsonResponse({'message': True})
    else:
        return JsonResponse({'message': False})

