from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from Farmers.models import Item as FarmerItem
from Shopkeeper.models import Item as ShopkeeperItem
from Auth.models import register

# Create your views here.
@login_required
def Admin(request):
    return render(request, 'Admin/Admin.html')

@login_required
def Dashboard(request):
    return render(request, 'Admin/Dashboard.html')

@login_required
def UserManagement(request):
    users = register.objects.all()
    context = { 'users': users }
    return render(request, 'Admin/UserManagement.html', context)

@login_required
def delete_user(request, user_id):
    user = get_object_or_404(register, id=user_id)
    if request.method == "POST":
        user.delete()
        messages.success(request, "User deleted.")
    return redirect('user_management')

def FarmerInventory(request):
    items = FarmerItem.objects.all().order_by('id')
    
    if request.method == 'POST':
        item_id = request.POST.get('id')
        FarmerItem.objects.filter(id=item_id).delete()
        messages.success(request, "Item deleted successfully.")
    return render(request, 'Admin/FarmerInventory.html', { 'items': items })

def ShopkeeperInventory(request):
    items = ShopkeeperItem.objects.all().order_by('id')
    
    if request.method == 'POST':
        item_id = request.POST.get('id')
        ShopkeeperItem.objects.filter(id=item_id).delete()
        messages.success(request, "Item deleted successfully.")
    return render(request, 'Admin/ShopkeeperInventory.html', { 'items': items })

def Admin_logout(request):
    logout(request)
    return redirect('LandingPage')