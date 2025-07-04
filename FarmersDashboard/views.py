from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
@login_required
def Admin_Dashboard(request):
    return render(request, 'FarmersDashboard/dashboard.html')

def Admin_Dashboard_logout(request):
    logout(request)
    return redirect('landing_page')