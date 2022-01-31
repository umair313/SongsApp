from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class UserRegisterationForm(UserCreationForm):
    class Meta:
        fields = ['username', 'email']
        model = get_user_model()
