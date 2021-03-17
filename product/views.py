from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Count
from .models import Product, ProductCategory, ProductImages


def product_list(request):
    categories = ProductCategory.objects.annotate(total_products=Count('product'))

    products = Product.objects.all()
    paginator = Paginator(products, 10)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    product_category = ProductCategory.objects.all
    context = {
        'products': products,
        'product_category': product_category,
        'categories': categories

    }
    return render(request, 'product/product_list.html', context)


def product_detail(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    product_images = ProductImages.objects.filter(product=product)
    context = {
        'product': product,
        'product_images': product_images

    }
    return render(request, 'product/product_detail.html', context)
