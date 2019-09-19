from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django import forms
import string
from django.utils.translation import ugettext_lazy as _

class UserSignupForm(UserCreationForm):

    def clean_username(self):
        username = self.cleaned_data["username"]
        if get_user_model().objects.filter(username__iexact=username).exists():
            print("user exist")
            raise forms.ValidationError("username taken, try another...")
        return username


class UserLoginForm(AuthenticationForm):

    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(username)s and password. Password is case-sensitive"
        ),
        'inactive': _("This account is inactive."),
    }

    def clean_username(self):
        username = self.cleaned_data["username"]
        _user = get_user_model().objects.filter(username__iexact=username)
        if _user.exists():
        #since our signup form is designed to store case insensitive username,
        #only one user will be returned by the filter. we can index with [0]
            username = _user.first().username
        return username
