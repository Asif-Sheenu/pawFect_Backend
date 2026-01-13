from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterSerializer (serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    class Meta :
        model =User
        fields = ['name','email','password','confirm_password']

    def create (self,validated_data ):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer (serializers.Serializer):
    email= serializers.EmailField()
    password = serializers.CharField(write_only = True)
   
    def validate (self, data):
        user = authenticate(**data)
        if not user:
            raise serializers.ValidationError("invalid credentials")
        return user
    

 