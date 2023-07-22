# accounts/urls.py
from django.urls import path
from account import views 

from .views import register


urlpatterns = [
    path("register/", views.register, name="register"),
]