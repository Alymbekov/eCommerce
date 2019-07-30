from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from apps.users.forms import UserCreationFormOwn
from apps.users.models import User, Profile


class SignupView(CreateView):
    form_class = UserCreationFormOwn
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class CabinetView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "cabinet.html"
    def get_object(self):
        return self.request.user

