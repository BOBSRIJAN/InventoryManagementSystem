from django.shortcuts import render
from Auth.decorators import custom_login_required
# Create your views here.
@custom_login_required
def user_dashboard(request):
    return render(request, 'User/UserDashboard.html')