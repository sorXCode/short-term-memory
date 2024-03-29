from django.urls import path
from .views import Signup, HomeView, Login, MemoryCreateView, MemoryEditView
from django.contrib.auth.views import LogoutView

app_name = 'stm'
urlpatterns = [
    path("signup/", Signup.as_view(), name="signup"),
    path("", HomeView.as_view(), name="home"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", LogoutView.as_view(template_name="stm/home.html"), name="logout"),
    path("create/", MemoryCreateView.as_view(), name="create"),
    path("edit/<pk>", MemoryEditView.as_view(), name="edit"),
]
