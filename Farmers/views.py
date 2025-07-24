from django.shortcuts import render, redirect
from Auth.decorators import custom_login_required
from django.conf import settings
from Farmers.models import Item
from Farmers.api import Ai
from django.contrib import messages
from datetime import datetime, date, timedelta
from django.core.files.storage import FileSystemStorage
import os
import re


@custom_login_required
def Farmers(request):
    Name = request.session.get('username')
    Email = request.session.get('Email')
    Role = request.session.get('role')

    user = {
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

    if request.method == "POST":
        action = request.POST.get("action")
        item_id = request.POST.get("id")
        search_term = request.POST.get("search_term")
        search_by = request.POST.get("search_by")

        try:
            price = float(request.POST["price"])
            add_date = datetime.strptime(
                request.POST["add_date"], "%Y-%m-%d").date()
            exp_date = datetime.strptime(
                request.POST["exp_date"], "%Y-%m-%d").date()

            today = datetime.now().date()
            max_date = today + timedelta(days=365)

            if price <= 0:
                messages.error(request, "Price must be greater than 0.")
                return redirect('Manage_items')

            if not (today < add_date <= max_date):
                messages.error(
                    request, "Add date must be a future date within 1 year.")
                return redirect('Manage_items')

            if not (today < exp_date <= max_date):
                messages.error(
                    request, "Expire date must be a future date within 1 year.")
                return redirect('Manage_items')

            if exp_date <= add_date:
                messages.error(request, "Expire date must be after Add date.")
                return redirect('Manage_items')

        except (ValueError, KeyError):
            messages.error(request, "Invalid input for price or dates.")
            return redirect('Manage_items')

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
            item.exp_date = request.POST["exp_date"]
            item.save()
            messages.success(request, "Item updated successfully")

        elif action == "delete" and item_id:
            Item.objects.filter(id=item_id, userid=user_id).delete()
            messages.error(request, "Item deleted successfully")

        elif action == "search":
            if search_term:
                if search_by == "name":
                    items = Item.objects.filter(
                        name__icontains=search_term, userid=user_id)
                elif search_by == "category":
                    items = Item.objects.filter(
                        category__icontains=search_term, userid=user_id)
                elif search_by == "date":
                    items = Item.objects.filter(
                        exp_date__icontains=search_term, userid=user_id)
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

            remaining_life = (exp_date - datetime.now()
                              ).total_seconds() / (60 * 60 * 24)
            used_percent = 100 - \
                int((remaining_life / total_life) *
                    100) if total_life > 0 else 100
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

    non_expired = [(item, used_percent)
                   for item, used_percent, _ in non_expired]
    expired = [(item, used_percent) for item, used_percent, _ in expired]

    for item, _ in expired:
        item.isExpired = True
        item.save()

    return render(request, "Farmers/InventoryReports.html", {
        "pie_chart_data": pie_chart_data,
        "total_quantity": total_quantity,
        "non_expired_items": non_expired,
        "expired_items": expired,
        "total": total_quantity,
    })


@custom_login_required
def Market_places(request):
    search_term = request.POST.get("search_term")
    search_by = request.POST.get("search_by")
    user_id = request.session.get('user_id')

    if search_term:
        if search_by == "name":
            items = Item.objects.filter(
                name__icontains=search_term, userid=user_id)
        elif search_by == "category":
            items = Item.objects.filter(
                category__icontains=search_term, userid=user_id)
        elif search_by == "date":
            items = Item.objects.filter(
                exp_date__icontains=search_term, userid=user_id)
        else:
            items = Item.objects.filter(userid=user_id)
        return render(request, "Farmers/MarketPlaces.html", {'items': items})

    items = Item.objects.filter(userid=user_id, isExpired=False)
    Market_places = items.filter(isInMarketPlaces=True, userid=user_id)
    return render(request, "Farmers/MarketPlaces.html", {'items': items, 'Market_places': Market_places})


@custom_login_required
def Market_places_send_items(request, id):
    try:
        update = Item.objects.get(id=id)
    except Item.DoesNotExist:
        messages.error(request, "Item not found.")
        return redirect('Market_places')

    if request.method == "POST":
        name = request.POST.get("name")
        quantity = request.POST.get("quantity")
        category = request.POST.get("category")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image = request.FILES.get("image")

        if all([name, quantity, category, price, description]):

            if not update.isInMarketPlaces and not image and not update.image:
                messages.error(
                    request, "Please upload an image before submitting to the marketplace.")
            else:
                update.name = name
                update.quantity = quantity
                update.category = category
                update.price = price
                update.description = description

                if image:
                    update.image = image

                update.isInMarketPlaces = True
                update.save()
                messages.success(
                    request, "Item successfully updated and sent to marketplace.")
                return redirect('Market_places')
        else:
            messages.error(request, "All fields are required.")

    return render(request, 'Farmers/Update.html', {'items': update})


def Delete_market_item(request, id):
    try:
        item = Item.objects.get(id=id)

        image_path = os.path.join(settings.MEDIA_ROOT, str(item.image))

        if os.path.exists(image_path):
            os.remove(image_path)

        item.isInMarketPlaces = False
        item.image = None
        item.save()
        messages.success(
            request, "Item image deleted and removed from marketplace.")
    except Item.DoesNotExist:
        messages.error(request, "Item not found.")
    return redirect('Market_places')


@custom_login_required
def AgriVision(request):
    prediction = None
    image_url = None

    if request.method == 'POST':
        uploaded_file = request.FILES.get("image")

        if not uploaded_file:
            messages.error(request, "Please upload an image.")
            return redirect('AgriVision')

        fs = FileSystemStorage(
            location=os.path.join(settings.BASE_DIR, 'media'))
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_path = os.path.join(settings.BASE_DIR, 'media', filename)
        image_url = fs.url(filename)

        pro = os.getenv('prompt')
        raw_prediction = Ai(prompt=pro, image=file_path)
        prediction = raw_prediction.replace('*', '').strip()

    return render(request, "Farmers/AgriVision.html", {
        'image_url': image_url,
        'prediction': prediction
    })


@custom_login_required
def AgriBot(request):
    return render(request, "Farmers/AgriBot.html")


def Farmers_logout(request):
    request.session.flush()
    return redirect('LandingPage')