from django.shortcuts import render, redirect
from Auth.decorators import custom_login_required

# Create your views here.
@custom_login_required
def Farmers(request):
    Name = request.session.get('username')
    Email = request.session.get('Email')
    Role = request.session.get('role')

    user  = {
        'Name': Name,
        'Email': Email, 
        'Role': Role,
    }
    
    if (not Email) and (not Name) and (not Role): 
        return redirect('login')
    
    return render(request, 'Farmers/FarmerDashboard.html', {'user': user})


def Farmers_logout(request):
    request.session.flush()
    return redirect('LandingPage')