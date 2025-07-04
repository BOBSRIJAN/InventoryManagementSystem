from django.shortcuts import render, redirect

# Create your views here.
def login(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        role = request.POST.get('role')
        password = request.POST.get('password')
    
    return render(request, 'LoginLogout/login.html')

def logout(request):
    return redirect('landing_page')
    
def register(request):
    return render(request, 'LoginLogout/register.html')