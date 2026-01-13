from django.shortcuts import render
# from rest_framework.generics import CreateAPIView
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
# Create your views here.


class RegisterView(APIView):
    def post(self , request ):
        serializer = RegisterSerializer (data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data

            refresh = RefreshToken.for_user(user)
            access = refresh.access_token

            return Response({
                "message": "Login successful",
                "access": str(access),
                "refresh": str(refresh),
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "is_superuser": user.is_superuser,
                    "is_staff": user.is_staff,
                }
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

