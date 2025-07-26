from django.urls import path
from .views import *

urlpatterns = [
    path('farmers/', Farmers, name='Farmers'),
    path("farmers_manage_items/", Manage_items, name="Manage_items"),
    path("farmers_inventory_reports/", Inventory_reports, name="Inventory_reports"),
    path("farmers_market_places/", Market_places, name="Market_places"),
    path("farmers_market_places_send_items/<str:id>/", Market_places_send_items, name="Market_places_send_items"),
    path("farmers_delete_market_item/<str:id>/", Delete_market_item, name="delete_market_item"),
    path('farmers_agri_vision/', AgriVision, name='AgriVision'),
    path('farmers_agri_bot/', AgriBot, name='AgriBot'),
    path("farmers_customer_feedback/",Customer_feedback, name="CustomerFeedback"),
    path('farmers_logout/', Farmers_logout, name='Farmers_logout'),
]