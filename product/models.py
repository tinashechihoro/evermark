from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    """
    Contains all product information
    """
    CONDITION_CHOICES = (
        ('New', 'New'),
        ('Old', 'Old'),
        ('Used', 'Used'),
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    condition = models.CharField(max_length=200, choices=CONDITION_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    """
    Product Category
    """
    category_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products_images/', blank=True, null=True)

    def __str__(self):
        return self.category_name
