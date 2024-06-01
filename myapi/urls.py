from django.urls import path
from . import views
from .lib import auth

urlpatterns = [
    path('hello-world', views.hello_world, name='hello_world'),
    path('login', auth.login, name='login'),
    path("register", auth.register, name="register"),
    path("logout", auth.logout, name="logout"),
]