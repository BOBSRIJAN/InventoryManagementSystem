from django.urls import path
from .views import *

urlpatterns = [
    path('shopkeeper/', Shopkeeper, name='Shopkeeper'),
    path("shopkeeper_manage_items/", Manage_items, name="Shopkeeper_Manage_items"),
    path("shopkeeper_inventory_reports/", Inventory_reports, name="Shopkeeper_Inventory_reports"),
    path("shopkeeper_market_places/", Market_places, name="Shopkeeper_Market_places"),
    path("shopkeeper_market_places_send_items/<str:id>/", Market_places_send_items, name="Shopkeeper_Market_places_send_items"),
    path("shopkeeper_delete_market_item/<str:id>/", Delete_market_item, name="Shopkeeper_delete_market_item"),
    path("shopkeeper_customer_feedback/", Customer_feedback, name="Shopkeeper_Customer_Feedback"),
    path('shopkeeper_logout/', Shopkeeper_logout, name='shopkeeper_logout'),
]