from django.contrib import admin

from .models import Product, ProductCategory, Brand, ProductImages


class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['category_name']


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'created_at']


admin.site.register(Product, ProductModelAdmin)

admin.site.register(ProductCategory)
admin.site.register(Brand)
admin.site.register(ProductImages)
