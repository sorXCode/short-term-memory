from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserSignupForm, UserLoginForm
from .models import memory
from django.contrib.auth.views import LoginView, PasswordChangeView


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


class Login(LoginView):
    form_class = UserLoginForm
    template_name = "stm/login.html"
    redirect_field_name = "stm:home"


class HomeView(ListView):
    context_object_name = 'thoughts'
    model = memory
    template_name = 'stm/home.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class MemoryCreateView(LoginRequiredMixin, CreateView):
    model = memory
    template_name = "stm/create.html"
    fields = ('thought',)
    login_url = "stm:login"
    success_url = "stm:home"

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            form_object = form.save(commit=False)
            form_object.user_id = get_user_model().objects.get(username=request.user).id
            form.save()
            return redirect(self.success_url)
        else:
            return self.form_invalid(form)

class MemoryEditView(LoginRequiredMixin, UpdateView):
    model = memory
    template_name = "stm/update.html"
    fields = ('thought',)
    success_url = "stm:home"
    # login_url = "stm:login"