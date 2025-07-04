from django.urls import path
from .views import *

urlpatterns = [
    path('fadmin/', Admin_Dashboard, name='Admin_Dashboard'),
    path('admin/logout/', Admin_Dashboard_logout, name='Admin_Dashboard_logout'),
]
