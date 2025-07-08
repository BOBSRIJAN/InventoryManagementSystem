from django.contrib import admin
from .views import *
from django.urls import path, include

urlpatterns = [
    path('srijan/', admin.site.urls),
    path('', LandingPage, name='LandingPage'),
    path('contact/', ContactUs, name='ContactUs'),
    path('about/', AboutUs, name='AboutUs'),
    # my app's
    path('', include('Farmers.urls')),
    path('customAdmin/', include('Admin.urls')),
    path('login/', include('Auth.urls')),
]
