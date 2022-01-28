from django.shortcuts import redirect, render
from .forms import UserRegisterationForm
# Create your views here.

def home(request):
    return render(request, 'account/default.html')


def register_user(request):
    registeration_form=UserRegisterationForm()
    if request.method=='POST':
        registeration_form=UserRegisterationForm(request.POST)
        if registeration_form.is_valid():
            registeration_form.save()
            return redirect('login')
    context = {
        'title':'Register',
        'form' : registeration_form
    }
    return render(request, 'account/register.html', context=context)


def userhome(request):
    return render(request, 'account/userhome.html', {'title':"Home SongsApp"})
