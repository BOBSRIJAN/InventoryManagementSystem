from django.shortcuts import render
from datetime import datetime, timedelta
from Auth.decorators import custom_login_required
# Create your views here.
@custom_login_required
def user_dashboard(request):
    launch_date = datetime.now() + timedelta(days=7)
    now = datetime.now()
    time_left = launch_date - now

    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    context = {
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds,
    }
    return render(request, 'User/UserDashboard.html', context)