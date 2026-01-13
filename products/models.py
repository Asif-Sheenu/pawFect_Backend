from django.db import models

# Create your models here.



class Product(models.Model):

    STATUS_CHOICES = (
        ("active", "Active"),
        ("inactive", "Inactive"),
    )

    CATEGORY_CHOICES = (
        ("dog", "Dog"),
        ("cat", "Cat"),
        
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField()
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )
    old_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    new_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="active"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
