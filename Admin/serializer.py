from rest_framework import serializers
from products.models import  Product
from orders.models import  Order
from Accounts.models import  User
# from Accounts.models import  User


# Product section 

class AdminFetchProductSerializer(serializers.ModelSerializer):
    class Meta :
        model= Product
        fields = ["id","name","description","image","category","old_price","new_price","status","created_at",]

class AdminUpdateProductSerializer(serializers.ModelSerializer):
    class Meta :
        model = Product
        fields = ["id","name","description","image","category","old_price","new_price",]
 
        
#  Order section 

class OrderListSerializer(serializers.Serializer):
    order_id = serializers.IntegerField(source="id")
    customer = serializers.CharField(source='full_name')
    email = serializers.EmailField()
    total = serializers.DecimalField(max_digits=10, decimal_places=2)
    status = serializers.CharField()
    created_at = serializers.DateTimeField()

class OrderEditSerializer(serializers.ModelSerializer):
    class Meta:
        model= Order
        fields=["status"]



# admin dashboard 

    
class AdminDashboardSerializer(serializers.Serializer):
    total_orders = serializers.IntegerField()
    total_users = serializers.IntegerField()
    total_products = serializers.IntegerField()
    total_revenue = serializers.DecimalField(max_digits=10, decimal_places=2)




       
# user mgmt         


class AdminUserSerializer(serializers.ModelSerializer):
    is_blocked = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "email",
            "is_active",
            "is_blocked",
           
        ]

    def get_is_blocked(self, obj):
         return not obj.is_active