from django.shortcuts import render, redirect
from Auth.decorators import custom_login_required
# Create your views here.
@custom_login_required
def Farmers(request):
    return render(request, 'Farmers/dashboard.html')

def Farmers_logout(request):
    request.session.flush()
    return redirect('LandingPage')