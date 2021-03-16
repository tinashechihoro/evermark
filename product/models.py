from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class ProductImages(models.Model):
    product = models.ForeignKey('Product', models.CASCADE)
    image = models.ImageField(upload_to='products_images/', blank=True, null=True)

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'

    def __str__(self):
        return self.product.name


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
    category = models.ForeignKey('ProductCategory', on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    city = models.CharField(max_length=200, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    """
    Product Category
    """
    category_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products_images/', blank=True, null=True)
    slug = models.SlugField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'

    def save(self, *args, **kwargs):
        if not self.slug and  self.category_name:
            self.slug = slugify(self.category_name)
            super(ProductCategory,self).save(*args, **kwargs)

    def __str__(self):
        return self.category_name


class Brand(models.Model):
    """
    Brand
    """
    brand_name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True, max_length=200)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def save(self, *args, **kwargs):
        if not self.slug and not self.brand_name:
            self.slug = slugify(self.brand_name)
            super(Brand, self).save(*args, **kwargs)

    def __str__(self):
        return self.brand_name
