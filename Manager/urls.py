from django.contrib import admin
from .views import *
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPage, name='LandingPage'),
    path('contact/', ContactUs, name='ContactUs'),
    path('about/', AboutUs, name='AboutUs'),
    path('', include('Farmers.urls'), name='farmers'),
    path('customAdmin/', include('Admin.urls'), name='customAdmin'),
    path('login/', include('LoginLogout.urls'), name='login'),
]
