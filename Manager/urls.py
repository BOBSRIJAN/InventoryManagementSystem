from django.contrib import admin
from .views import *
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPage, name='LandingPage'),
    path('contact/', ContactUs, name='ContactUs'),
    path('about/', AboutUs, name='AboutUs'),
    path('dashboard/', include('FarmersDashboard.urls'), name='dashboard'),
    path('custom_admin/', include('Admin.urls'), name='custom_admin'),
    path('login/', include('LoginLogout.urls'), name='login'),
]
