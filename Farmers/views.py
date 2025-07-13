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
    search_term = ""
    search_by = ""

    if request.method == "POST":
        action = request.POST.get("action")
        item_id = request.POST.get("id")
        search_term = request.POST.get("search_term")
        search_by = request.POST.get("search_by")

        if action == "add":
            Item.objects.create(
                name=request.POST["name"],
                quantity=request.POST["quantity"],
                category=request.POST["category"],
                price=request.POST["price"],
                add_date=request.POST["add_date"],
                exp_date=request.POST["exp_date"],
                
            )
            messages.success(request, "Item Added Successfully")
        
        elif action == "update" and item_id:
            item = Item.objects.get(id=item_id)
            item.name = request.POST["name"]
            item.quantity = request.POST["quantity"]
            item.category = request.POST["category"]
            item.price = request.POST["price"]
            item.add_date = request.POST["add_date"]
            item.exp_date=request.POST["exp_date"]
            item.save()
            messages.success(request, "Item updated successfully")
        
        elif action == "delete" and item_id:
            Item.objects.filter(id=item_id).delete()
            messages.error(request, "Item deleted successfully")
            
        elif action == "search":
            if search_term:
                if search_by == "name":
                    items = Item.objects.filter(name__icontains=search_term)
                elif search_by == "category":
                    items = Item.objects.filter(category__icontains=search_term)
                elif search_by == "date":
                    items = Item.objects.filter(exp_date__icontains=search_term)
                else:
                    items = Item.objects.all()
                
                return render(request, 'Farmers/Manage_items.html', {
                    "items": items,
                    "search_term": search_term,
                    "search_by": search_by,
                    "edit_item": None
                })

        return redirect('Manage_items')

    # For GET requests
    items = Item.objects.all().order_by("-id")
    edit_item = None
    edit_id = request.GET.get("edit")

    if edit_id:
        try:
            edit_item = Item.objects.get(id=edit_id)
        except Item.DoesNotExist:
            messages.error(request, "Item not found or does not exist")

    return render(request, 'Farmers/Manage_items.html', {
        "items": items,
        "edit_item": edit_item,
        "search_term": search_term,
        "search_by": search_by
    })


def Inventory_reports(request):
    pass
    return render(request, "Farmers/InventoryReports.html")


def Farmers_logout(request):
    request.session.flush()
    return redirect('LandingPage')