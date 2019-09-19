from django.shortcuts import render, redirect, reverse
from django.views.generic import CreateView, ListView
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserSignupForm, UserLoginForm
from .models import memory
from django.contrib.auth.views import LoginView


class Signup(CreateView):
    form_class = UserSignupForm
    template_name = 'stm/signup.html'

    def post(self, request, *args, **kwargs):
        signup = self.form_class(request.POST)
        if signup.is_valid():
            username = signup.cleaned_data['username']
            password = signup.cleaned_data["password1"]
            signup.save()
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('stm:home')
        return render(request, self.template_name, {'form': self.form_class(request.POST)})


class HomeView(ListView):
    context_object_name = 'thoughts'
    model = memory
    template_name = 'stm/home.html'

class Login(LoginView):
    form_class = UserLoginForm
    template_name = "stm/login.html"
    redirect_field_name = "stm:home"