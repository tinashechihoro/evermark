from django.urls import path
from .views import product_detail,product_list

app_name = 'product'
urlpatterns = [

    path('', product_list, name='product_list'),
    #path('<slug:category_slug>', product_list, name='product_list_category_slug'),
    path('<slug:product_slug>',product_detail, name='product_detail'),
]
