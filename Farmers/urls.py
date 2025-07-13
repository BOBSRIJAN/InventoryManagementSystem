from django.urls import path
from .views import *

urlpatterns = [
    path('farmers/', Farmers, name='Farmers'),
    path("manage_items/", Manage_items, name="Manage_items"),
    path("inventory_reports/", Inventory_reports, name="Inventory_reports"),
    path("market_places/", Market_places, name="Market_places"),
    path('farmers_logout/', Farmers_logout, name='Farmers_logout'),
]
