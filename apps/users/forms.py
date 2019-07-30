from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.users.models import User

class UserCreationFormOwn(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')