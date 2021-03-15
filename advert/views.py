from django.shortcuts import render
from .models import Advert

def advert_list(request):
    advert =  Advert.objects.all()
    context = {
        'advert':advert

    }
    return render(request,'advert/advert_list.html',context)