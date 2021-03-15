from django.conf import settings
from django.conf.urls.static import static


from django.urls import path
from .views import group_list

app_name = 'groups'
urlpatterns = [
                  path('', group_list,'group_list'),

              ]