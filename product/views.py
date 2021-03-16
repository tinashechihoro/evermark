from django.shortcuts import render
from .models import Product , ProductCategory


def product_list(request):
    products = Product.objects.all()
    product_category = ProductCategory.objects.all
    context = {
        'products': products,
        'product_category':product_category

    }
    return render(request, 'product/product_list.html', context)


def product_detail(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    context = {
        'product': product

    }
    return render(request, 'product/product_detail.html', context)
