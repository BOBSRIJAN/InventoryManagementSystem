from django.shortcuts import render, redirect
from Auth.decorators import custom_login_required
from .models import Item
from django.contrib import messages
from datetime import datetime, date

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
    user_id = request.session.get('user_id')
    print(user_id)
    
    if request.method == "POST":
        action = request.POST.get("action")
        item_id = request.POST.get("id")
        search_term = request.POST.get("search_term")
        search_by = request.POST.get("search_by")

        if action == "add":
            Item.objects.create(
                userid=user_id,
                name=request.POST["name"],
                quantity=request.POST["quantity"],
                category=request.POST["category"],
                price=request.POST["price"],
                add_date=request.POST["add_date"],
                exp_date=request.POST["exp_date"],
                
            )
            messages.success(request, "Item Added Successfully")
        
        elif action == "update" and item_id:
            item = Item.objects.get(id=item_id, userid=user_id)
            item.name = request.POST["name"]
            item.quantity = request.POST["quantity"]
            item.category = request.POST["category"]
            item.price = request.POST["price"]
            item.add_date = request.POST["add_date"]
            item.exp_date=request.POST["exp_date"]
            item.save()
            messages.success(request, "Item updated successfully")
        
        elif action == "delete" and item_id:
            Item.objects.filter(id=item_id, userid=user_id).delete()
            messages.error(request, "Item deleted successfully")
            
        elif action == "search":
            if search_term:
                if search_by == "name":
                    items = Item.objects.filter(name__icontains=search_term, userid=user_id)
                elif search_by == "category":
                    items = Item.objects.filter(category__icontains=search_term, userid=user_id)
                elif search_by == "date":
                    items = Item.objects.filter(exp_date__icontains=search_term, userid=user_id)
                else:
                    items = Item.objects.filter(userid=user_id)
                
                return render(request, 'Farmers/Manage_items.html', {
                    "items": items,
                    "search_term": search_term,
                    "search_by": search_by,
                    "edit_item": None
                })

        return redirect('Manage_items')

    # For GET requests
    items = Item.objects.filter(userid=user_id).order_by("-id")
    edit_item = None
    edit_id = request.GET.get("edit")

    if edit_id:
        try:
            edit_item = Item.objects.get(id=edit_id, userid=user_id)
        except Item.DoesNotExist:
            messages.error(request, "Item not found or does not exist")

    return render(request, 'Farmers/Manage_items.html', {
        "items": items,
        "edit_item": edit_item,
        "search_term": search_term,
        "search_by": search_by
    })

@custom_login_required
def Inventory_reports(request):
    user_id = request.session.get('user_id')
    items = Item.objects.filter(userid=user_id)

    name_data = {}
    for item in items:
        name_data[item.name] = name_data.get(item.name, 0) + item.quantity

    total_quantity = sum(name_data.values())
    pie_chart_data = []
    
    start_degree = 0
    for i, (name, quantity) in enumerate(name_data.items()):
        hue = (i * 60) % 360
        color = f"hsl({hue}, 70%, 60%)"
        degree = (quantity / total_quantity) * 360 if total_quantity > 0 else 0
        end_degree = start_degree + degree

        pie_chart_data.append({
            "name": name,
            "color": color,
            "start_degree": start_degree,
            "end_degree": end_degree,
            "quantity": quantity,
        })

        start_degree = end_degree 

    non_expired = []
    expired = []

    for item in items:
        try:
            exp_date = datetime.strptime(item.exp_date, "%Y-%m-%d")
            add_date = datetime.strptime(item.add_date, "%Y-%m-%d")

            total_life = (exp_date - add_date).days

            remaining_life = (exp_date - datetime.now()).total_seconds() / (60 * 60 * 24)
            used_percent = 100 - int((remaining_life / total_life) * 100) if total_life > 0 else 100
            used_percent = min(max(used_percent, 0), 100)

            if date.today() > exp_date.date():
                expired.append((item, used_percent, exp_date))
            else:
                non_expired.append((item, used_percent, exp_date))

        except Exception:
            exp_date = datetime.max
            used_percent = 100
            expired.append((item, used_percent, exp_date))

    non_expired.sort(key=lambda x: x[2])
    expired.sort(key=lambda x: x[2])

    non_expired = [(item, used_percent) for item, used_percent, _ in non_expired]
    expired = [(item, used_percent) for item, used_percent, _ in expired]

    return render(request, "Farmers/InventoryReports.html", {
        "pie_chart_data": pie_chart_data,
        "total_quantity": total_quantity,
        "non_expired_items": non_expired,
        "expired_items": expired,
        "total":total_quantity,
    })

@custom_login_required
def Market_places(request):
    return render(request, "Farmers/MarketPlaces.html")
    

def Farmers_logout(request):
    request.session.flush()
    return redirect('LandingPage')