from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import UserRegisterationForm
from songs.models import Playlist
# Create your views here.





class RegisterUserView(CreateView):
    form_class = UserRegisterationForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        self.object = form.save()
        Playlist.objects.create(owner=self.object)
        return super(RegisterUserView, self).form_valid(form)


