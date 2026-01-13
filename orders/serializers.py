from rest_framework import serializers
from .models import  Order,OrderList,Product



class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())  # Accepts product ID

    class Meta :
        model= OrderList
        fields = ["product","price","quantity"]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many= True)
    class Meta:
        model = Order
        fields = [
                "id",
                "full_name",
                "email",
                "phone",
                "address",
                "subtotal",
                "discount",
                "taxes",
                "shipping",
                "total",
                "status",
                "created_at",
                "items",
            ]
    
    def create(self, validated_data):
       
        items_data= validated_data.pop("items")
        request = self.context["request"]
        user = request.user

        order = Order.objects.create(
            user=user,
            **validated_data
        )
        

        for item in items_data:
            product = Product.objects.get(id=item["product"].id if hasattr(item["product"], "id") else item["product"])

            OrderList.objects.create(
            order=order,
            product=product,
            price=item["price"],
            quantity=item["quantity"],
        )

        return order

