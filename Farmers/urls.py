from django.urls import path
from .views import *

urlpatterns = [
    path('farmers/', Farmers, name='Farmers'),
    path("manage_items/", Manage_items, name="Manage_items"),
    path('farmers_logout/', Farmers_logout, name='Farmers_logout'),
]
