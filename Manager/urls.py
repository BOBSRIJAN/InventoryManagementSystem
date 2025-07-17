from django.contrib import admin
from .views import *
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('srijan/', admin.site.urls),
    path('', LandingPage, name='LandingPage'),
    path('contact/', ContactUs, name='ContactUs'),
    path('about/', AboutUs, name='AboutUs'),
    path("dev's/", dev, name="dev"),
    # my app's
    path('customAdmin/', include('Admin.urls')),
    path('login/', include('Auth.urls')),
    path('', include('Farmers.urls')),
    path('Shopkeeper/', include('Shopkeeper.urls')),
    path('User/', include('User.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
