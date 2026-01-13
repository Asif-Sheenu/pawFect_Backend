from django.urls import path
from .views import CartView, AddToCartView, RemoveCartItemView

urlpatterns = [
    path("cart/", CartView.as_view(), name="cart"),
    path("add/", AddToCartView.as_view(), name="add-to-cart"),
    path("remove/<int:item_id>/", RemoveCartItemView.as_view(), name="remove-cart-item"),
]
