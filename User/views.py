from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from django.contrib import messages
from Auth.decorators import custom_login_required

# Create your views here.
@custom_login_required
def user_dashboard(request):
    UserName = request.session.get('username')
    UserEmail = request.session.get('Email')
    Role = request.session.get('role')
    if Role != 'user':
        messages.error(request, "your are not authorized to access this page")
        return redirect('LandingPage')
    return render(request, 'User/UserDashboard.html', {'UserName': UserName})

def user_logout(request):
    request.session.flush()
    return redirect('LandingPage')