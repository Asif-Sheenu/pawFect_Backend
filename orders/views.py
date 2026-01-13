from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import OrderSerializer
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.permissions import IsAuthenticated
from .models import Order
# Create your views here.


class PlaceOrderView(APIView):
    permission_classes=[IsAuthenticated]

    def post (self,request):
        try:

            serializer= OrderSerializer(data=request.data, context={"request":request})
            serializer.is_valid(raise_exception=True)
            order=serializer.save()
            return Response({"message":"order placed !","order":OrderSerializer(order).data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)

class OrderlistView(APIView):
    permission_classes=[IsAuthenticated]

    def get (self,request):
        try:
            orders = Order.objects.filter(user=request.user).order_by('-created_at')
            serializer =OrderSerializer(orders,many=True)
            return Response (serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)            
        
        