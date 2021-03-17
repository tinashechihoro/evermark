from django.shortcuts import render
from .models import Product, ProductCategory, ProductImages


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
    product_images = ProductImages.objects.filter(product=product)
    context = {
        'product': product,
        'product_images':product_images

    }
    return render(request, 'product/product_detail.html', context)
