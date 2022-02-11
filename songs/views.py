from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic as generic_views
from .models import Album, Track, Artist, Playlist
# Create your views here.

def homeView(request):
    return redirect('listing')

class ListView(LoginRequiredMixin, generic_views.View):
    login_url = 'login'
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


class ArtistListView(LoginRequiredMixin, generic_views.ListView):
    login_url = 'login'
    model = Artist
    template_name = 'app/artistlisting.html'


class AlbumListView(LoginRequiredMixin, generic_views.ListView):
    login_url = 'login'
    model = Album
    template_name = 'app/albumslisting.html'


class TrackDetailView(LoginRequiredMixin, generic_views.DetailView):
    login_url = 'login'
    model = Track
    context_object_name = 'track'
    template_name = 'app/track.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["liked_tracks"] = user.playlists.filter(name="Liked Songs").first().tracks.all()
        return context


class AlbumDetailView(LoginRequiredMixin, generic_views.DetailView):
    login_url = 'login'
    model = Album
    context_object_name = 'album'
    template_name = 'app/album.html'


class ArtistDetailView(LoginRequiredMixin, generic_views.DetailView):
    login_url = 'login'
    model = Artist
    context_object_name = 'artist'
    template_name = 'app/artist.html'


class LikeSongsPlaylistView(LoginRequiredMixin, generic_views.View):
    login_url = 'login'
    def get(self, request, *args, **kwargs):
        user = request.user
        playlist = Playlist.objects.get(name='Liked Songs', owner=user)
        tracks = playlist.tracks.all()
        return render(request, 'app/playlist.html', context={"tracks": tracks})


class PlaylistView(LoginRequiredMixin, generic_views.DetailView):
    login_url = 'login'
    model = Playlist
    login_url = 'login'
    template_name = 'app/playlist.html'
    context_object_name = 'playlist'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        playlist =  get_object_or_404(Playlist, name='Liked Songs', owner=user)
        context["liked_tracks"] = playlist.tracks.all()
        return context


class PlaylistDeleteView(LoginRequiredMixin, generic_views.DeleteView):
    model = Playlist
    template_name = 'app/playlist_confirm_delete.html'
    success_url = reverse_lazy('listing')


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


def createPlaylist(request, name):
    user = request.user
    try:
        object = Playlist.objects.get(name=name)
    except Playlist.DoesNotExist:
        object = None
    
    if object:
        return JsonResponse({
            "created" : False
        })

    object = Playlist.objects.create(name=name, owner = user)

    return JsonResponse({
        "created": True,
        "id": object.pk,
        "name": object.name
    })


def addTrackToPlaylist(request, playlist_id, track_id):
    user = request.user
    playlist = get_object_or_404(Playlist, id=playlist_id, owner=user)
    track = get_object_or_404(Track, id=track_id)
    playlist.tracks.add(track)
    return JsonResponse({
        "added": True
    })


def removeTrackFromPlaylist(request, playlist_id, track_id):
    user = request.user
    playlist = get_object_or_404(Playlist, id=playlist_id, owner=user)
    track = get_object_or_404(Track, id=track_id)
    playlist.tracks.remove(track)
    return JsonResponse({
        "removed": True
    })
