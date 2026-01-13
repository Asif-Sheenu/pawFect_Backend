from django.contrib.auth.models import BaseUserManager

class UserManager (BaseUserManager):
    def create_user (self , email, password=None, name = None):
        if not email :
            raise ValueError("Email is required !")

        email =self.normalize_email(email)
        user =self.model(name=name ,email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password, name= "Admin"):
        user = self.create_user(email,password,name)
        user.is_staff= True
        user.is_superuser= True
        user.is_active = True

        user.save(using=self._db)
        return user