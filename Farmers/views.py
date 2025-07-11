from django.shortcuts import render, redirect
from Auth.decorators import custom_login_required
from .models import Item
from django.contrib import messages
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

@custom_login_required
def Manage_items(request):
    if request.method == "POST":
        action = request.POST.get("action")
        item_id = request.POST.get("id")

        if action == "add":
            Item.objects.create(
                name=request.POST["name"],
                quantity=request.POST["quantity"],
                category=request.POST["category"],
                price=request.POST["price"]
            )
            messages.success(request, "Item Added Successfully")#this not shoing in the template add leater okk
        elif action == "update" and item_id:
            item = Item.objects.get(id=item_id)
            item.name = request.POST["name"]
            item.quantity = request.POST["quantity"]
            item.category = request.POST["category"]
            item.price = request.POST["price"]
            item.save()
        elif action == "delete" and item_id:
            Item.objects.filter(id=item_id).delete()

        return redirect('Manage_items')

    
    items = Item.objects.all().order_by("-id")
    edit_item = None
    edit_id = request.GET.get("edit")
    if edit_id:
        try:
            edit_item = Item.objects.get(id=edit_id)
        except Item.DoesNotExist:
            messages.error("item not found or dose not exist")
    return render(request, 'Farmers/Manage_items.html', {"items": items, "edit_item": edit_item})

def Farmers_logout(request):
    request.session.flush()
    return redirect('LandingPage')