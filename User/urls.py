
from .views import *
from django.urls import path

urlpatterns = [
    path("user_dashboard/", user_dashboard, name="user_dashboard"),
    path("user_logout/", user_logout, name="user_logout")
]