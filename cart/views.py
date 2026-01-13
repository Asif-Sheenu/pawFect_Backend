from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Cart, CartItem
from .serializers import CartSerializer, AddToCartSerializer
from products.models import Product


class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart,_ = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response( serializer.data, status=status.HTTP_202_ACCEPTED)


class AddToCartView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request):
        serializer = AddToCartSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product_id = serializer.validated_data["product_id"]
        quantity = serializer.validated_data["quantity"]

        cart, _ = Cart.objects.get_or_create(user=request.user)
        product = Product.objects.get(id=product_id)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product
        )

        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity

        cart_item.save()

        return Response(
            {"message": "Product added to cart"},
            status=status.HTTP_201_CREATED
        )


class RemoveCartItemView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, item_id):
        cart = Cart.objects.get(user=request.user)
        item = CartItem.objects.get(id=item_id, cart=cart)
        item.delete()
        return Response({"message": "Item removed"})
