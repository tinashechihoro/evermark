from django.contrib import admin

from .models import Product


class ProductModelAdmin(admin.ModelAdmin):
    list_display =  ['name','description','price','created_at']
admin.site.register(Product,ProductModelAdmin)
