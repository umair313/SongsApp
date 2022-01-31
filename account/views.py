from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import UserRegisterationForm

# Create your views here.

class HomeView(TemplateView):
    template_name = 'account/default.html'


class RegiserUserView(CreateView):
    form_class = UserRegisterationForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('login')


class ApplicationHomeView(TemplateView):
    template_name = 'account/userhome.html'
