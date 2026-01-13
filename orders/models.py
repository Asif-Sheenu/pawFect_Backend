from django.db import models
from Accounts.models import User
from products.models import Product
# Create your models here.


class Order (models.Model):

    STATUS_CHOICES= (
        ('Pending','PENDING'),
        ('Processing','PROCESSING'),
        ('Shipped','SHIPPED'),
        ('Delivered','DELIVERED'),
        ('Cancelled','CANCELLED'),
    )

    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='orders')
    
    full_name= models.CharField(max_length=100)
    email= models.EmailField()
    phone = models.IntegerField()
    address= models.CharField(max_length=100)

    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    taxes = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    shipping = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    status= models.CharField(max_length=20,choices=STATUS_CHOICES,default='Pending')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}-{self.full_name}"

class OrderList(models.Model):
    order= models.ForeignKey(Order,on_delete=models.CASCADE, related_name="items")    
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity= models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"
    