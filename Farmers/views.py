from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def Farmers(request):
    return render(request, 'Farmers/dashboard.html')

def Farmers_logout(request):
    logout(request)
    return redirect('LandinPgage')