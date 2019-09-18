from django.contrib.auth import get_user_model
from django.contrib.auth.forms import User, UserCreationForm

from django import forms
import string


class UserSignupForm(UserCreationForm):
    def clean_password(self):
        password = self.cleaned_data.get("password")
        must_contain = [string.digits, string.punctuation]
        for character in password:
            if character in must_contain:
                return password
        else:
            raise forms.ValidationError(
                self.error_messages["password must contain a number or punctuation"],
                code="invalid_password",
            )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if get_user_model().objects.filter(username__iexact=username).exists():
            raise forms.ValidationError(
                message="username taken, try another...", code="user exists")
        return username

        
    # def save(self):
    #     user = super().save(commit=False)
