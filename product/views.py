from django.shortcuts import render
from .models import Product


def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products

    }
    return render(request, 'product/product_list.html', context)


def product_detail(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    context = {
        'product': product

    }
    return render(request, 'index.html', context)
