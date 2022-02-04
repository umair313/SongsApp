from django.shortcuts import render
from django.views.generic import FormView
from .forms import SearchForm
from .models import Genre, Album, Track, Artist
# Create your views here.


class SearchView(FormView):

    def get(self, request, *args, **kwargs):
        genres = Genre.objects.all()
        albums = Album.objects.all()
        artists = Artist.objects.all()
        tracks = Track.objects.all()

        form = SearchForm()
        context = {
            'form': form,
            'tracks': tracks,
            'genres': genres,
            'albums': albums,
            'artists': artists
        }
        return render(request, 'search/search.html', context=context)

    def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['search']
            genres = Genre.objects.filter(name__search=query)
            albums = Album.objects.filter(name__search=query)
            tracks = Track.objects.filter(title__search=query)
            artists = Artist.objects.filter(name__search=query)
            context = {
                'form': form,
                'tracks': tracks,
                'genres': genres,
                'albums': albums,
                'artists': artists
            }
            return render(request, 'search/search.html', context=context)


