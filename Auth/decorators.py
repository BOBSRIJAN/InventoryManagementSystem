from django.shortcuts import redirect
from functools import wraps

def custom_login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if 'Email' not in request.session or 'role' not in request.session:
            return redirect('login') 
        return view_func(request, *args, **kwargs)
    return wrapper
