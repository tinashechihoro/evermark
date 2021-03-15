from django.conf import settings
from django.conf.urls.static import static


from django.urls import path
from .views import advert_list

app_name = 'advert'
urlpatterns = [
                  path('', advert_list,'advert_list'),

              ]