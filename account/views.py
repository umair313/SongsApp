from django.http import HttpResponse
from django.shortcuts import render

from .forms import UserRegisterationForm
# Create your views here.

def home(request):
    return render(request, 'account/default.html')


def register_user(request):
    registeration_form = UserRegisterationForm()
    if request.method == 'POST':
        registeration_form = UserRegisterationForm(request.POST)
        if registeration_form.is_valid():
            registeration_form.save()
            return HttpResponse("User Created")
    context = {
        'form' : registeration_form
    }
    return render(request, 'account/register.html', context = context)
