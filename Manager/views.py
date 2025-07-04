from django.shortcuts import render
from django.contrib.auth.models import User

def LandingPage(request):
    return render(request, 'LandingPage.html')

def AboutUs(request):
    return render(request, 'AboutUs.html')

def ContactUs(request):
    return render(request, 'ContactUs.html')
