from django.urls import path
from .views import *

urlpatterns = [
    path('farmers/', Farmers, name='Farmers'),
    path('farmers/logout/', Farmers_logout, name='farmers_logout'),
]
