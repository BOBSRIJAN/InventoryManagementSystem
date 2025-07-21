from django.urls import path
from .views import *

urlpatterns = [
    path('', Admin, name='custom_admin'),
    path("dashboard/", Dashboard, name="dashboard"),
    path("user_management/", UserManagement, name="user_management"),
    path('user/delete/<int:user_id>/', delete_user, name='delete_user'),
    path('admin/logout/', Admin_logout, name='admin_logout'),
]
