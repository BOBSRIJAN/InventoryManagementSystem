from django.shortcuts import render, redirect

def LandingPage(request):
    if request.method == 'POST':
        flag = request.POST.get('flag')
        if flag == 'user':
            Name = request.session.get('username')
            Email = request.session.get('Email') 
            Role = request.session.get('role')
            
            if Name and Email and Role:
                if Role == 'farmer':
                    return redirect('Farmers')
                elif Role == 'Shopkeeper':
                    return redirect('Farmers') 
                elif Role == 'user':
                    return redirect('Farmers')
        return redirect('login')

    return render(request, 'LandingPage.html')


def AboutUs(request):
    return render(request, 'AboutUs.html')

def dev(request):
    return render(request, 'dev.html')

def ContactUs(request):
    return render(request, 'ContactUs.html')
