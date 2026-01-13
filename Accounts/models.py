from django.db import models

# Create your models here.


from django.contrib.auth.models  import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

class User (AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100, blank = False)
    email = models.EmailField(unique=True)
    is_staff= models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined= models.DateTimeField(auto_now_add=True)

    objects= UserManager()

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS=['name']

    def __str__(self):
        return self.email


