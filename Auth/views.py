from django.shortcuts import render, redirect
from .models import register as user_register
from django.contrib import messages
import time 

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('Email')
        password = request.POST.get('password')
        
        try:
            user = user_register.objects.get(username = username, email = email)
        except user_register.DoesNotExist:
            user = None
        
        if user is not None and user.check_password(password):
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            request.session['Email'] = user.email
            request.session['role'] = user.role
            
            if user.role == 'farmer':
                return redirect('Farmers')
            
            elif user.role == 'Shopkeeper':
                return redirect('Shopkeeper')
            
            elif user.role == 'user':
                return
            
            else:
                messages.error(request, "Invalid user")
        else:
            messages.error(request, "you are not a valid user!")
            time.sleep(2)
            return redirect("register")
    return render(request, 'Auth/login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('Email')
        role = request.POST.get('role')
        password = request.POST.get('password')
        
        try:
            new_user = user_register(
                username=username, 
                email=email, 
                role=role, 
                password=password )
            new_user.save()
            
        except Exception as e:
            messages.error(request, f"User email already exists")
            
        return redirect('login')
    
    return render(request, 'Auth/register.html')