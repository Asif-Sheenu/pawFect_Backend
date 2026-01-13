from django.contrib import admin
from django.urls import path,include
from .views import PlaceOrderView, OrderlistView


urlpatterns = [
    path('order/', PlaceOrderView.as_view(), name="place_order"),
    path('orderlist/', OrderlistView.as_view(), name="order_list"),
    
    ]