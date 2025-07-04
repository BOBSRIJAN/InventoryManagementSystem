from django.urls import path
from .views import *

urlpatterns = [
    path('', Admin, name='custom_admin'),
    path("dashboard/", Dashboard, name="dashboard"),
    path('admin/logout/', Admin_logout, name='admin_logout'),
]
