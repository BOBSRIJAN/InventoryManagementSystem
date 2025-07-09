from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
@login_required
def Admin(request):
    return render(request, 'Admin/Admin.html')

@login_required
def Dashboard(request):
    return render(request, 'Admin/Dashboard.html')

def Admin_logout(request):
    logout(request)
    return redirect('LandingPage')