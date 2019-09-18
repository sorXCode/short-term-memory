from django.urls import path
from .views import Signup

app_name = 'stm'
urlpatterns = [
    path("signup/", Signup.as_view(), name="signup")
]
