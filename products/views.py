from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .permissions import IsAdminOrReadOnly
from .models import Product
from .serializers import ProductSerializer
# for fltr
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend



class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes= [IsAdminOrReadOnly]

    filter_backends = [SearchFilter,DjangoFilterBackend]
    search_fields = ["name","description"]
    filterset_fields= ["category", "status"]
