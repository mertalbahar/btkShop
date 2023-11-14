from django.shortcuts import render
from .models import ShopSetting


def index(request):
    setting = ShopSetting.objects.get(pk=1)
    page = request.get_full_path()
    page = page[1:]
    
    if page == '':
        page = 'Anasayfa'
    else:
        page
    
    context = {
        'page': page,
        'setting': setting
    }
    return render(request, 'home/index.html', context)


def contact(request):
    setting = ShopSetting.objects.get(pk=1)
    page = request.get_full_path()
    page = page[1:]
    
    if page == '':
        page = 'Anasayfa'
    else:
        page
    
    context = {
        'page': page,
        'setting': setting
    }
    return render(request, 'home/contact.html', context)


def about(request):
    setting = ShopSetting.objects.get(pk=1)
    page = request.get_full_path()
    page = page[1:]
    
    if page == '':
        page = 'Anasayfa'
    else:
        page
    
    context = {
        'page': page,
        'setting': setting
    }
    return render(request, 'home/about.html', context)


def reference(request):
    setting = ShopSetting.objects.get(pk=1)
    page = request.get_full_path()
    page = page[1:]
    
    if page == '':
        page = 'Anasayfa'
    else:
        page
    
    context = {
        'page': page,
        'setting': setting
    }
    return render(request, 'home/reference.html', context)