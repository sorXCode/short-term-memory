from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from django.contrib.auth.views import LoginView
from .forms import UserSignupForm



class Signup(CreateView):
    form_class = UserSignupForm
    template_name = 'stm/signup.html'
    # context_object_name = 'signup'
    def post(self, *args, **kwargs):
        signup = self.form_class()
        if signup.is_valid():
            signup.save()
            redirect()

class HomeView(ListView):
    