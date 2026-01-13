from django.shortcuts import render
from rest_framework.views import APIView
from products.models import Product
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .serializer import AdminFetchProductSerializer,AdminUpdateProductSerializer, OrderListSerializer , OrderEditSerializer,AdminDashboardSerializer,AdminUserSerializer
from rest_framework import status
from orders.models import Order
from Accounts.models import User
from django.db.models import Sum
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


# Create your views here.

class ProductfetchView(APIView):
    permission_classes=[IsAuthenticated,IsAdminUser]
    def get (self,request):
        data= Product.objects.all()
        serializer=  AdminFetchProductSerializer(data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class ProductAddView(APIView):
    permission_classes=  [IsAdminUser]
    def post (self,request ):
        serializers = AdminUpdateProductSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response({"message":"product added successfully"},status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    

class ProductUpdateView(APIView):
    permission_classes=[IsAdminUser]
    def patch(self ,request,pk):
        product = Product.objects.get(pk=pk)
        serializers= AdminUpdateProductSerializer(product,data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)



# Order Section


class OrderListView(APIView):
    permission_classes=[IsAdminUser]
    def get(self,request):
        try:
            orders = Order.objects.prefetch_related('items__product').order_by('-created_at')
            serializers= OrderListSerializer(orders,many=True)
            return Response(serializers.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":"Something went wrong","details":str(e)},status=status.HTTP_400_BAD_REQUEST)


class OrderEditView(APIView):
    permission_classes=[IsAdminUser]
    def patch(self,request,pk):
        try:
            order= Order.objects.get(pk=pk)
            serializers= OrderEditSerializer(order,data=request.data, partial =True)
            if serializers.is_valid():
                serializers.save()
                return Response({"message":"status changed successfully"}, status=status.HTTP_200_OK)
            else:
                return Response(serializers.errors, status=400)
        except Exception as e:
            return Response({"error":"Something went wrong","details":str(e)},status=status.HTTP_400_BAD_REQUEST)



#  admin dashboard


class AdminDashboardView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        data = {
            "total_orders": Order.objects.count(),
            "total_users": User.objects.count(),
            "total_products": Product.objects.count(),
            "total_revenue": Order.objects.aggregate(
                total=Sum("total")
            )["total"] or 0
        }

        serializer = AdminDashboardSerializer(data)
        return Response(serializer.data)
    

# User Mgmt    

class AdminUserListView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        users = User.objects.filter(is_staff=False)
        serializer = AdminUserSerializer(users, many=True)
        return Response(serializer.data)




class AdminUserBlockView(APIView):
    permission_classes = [IsAdminUser]

    def patch(self, request, pk):
        user = get_object_or_404(User, pk=pk)

        if user.is_staff :
            return Response(
                {"detail": "Admins cannot be blocked"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user.is_active = not user.is_active
        user.save()

        serializer = AdminUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)