from django.shortcuts import render
from home.models import ShopSetting


def index(request):
    setting = ShopSetting.objects.get(pk=1)
    page = request.get_full_path()
    page = page.split('/')
    page = page[1]
    
    if page == 'product':
        page = 'Ürünler'
    else:
        page
    
    context = {
        'page': page,
        'setting': setting
    }
    return render(request, 'product/index.html', context)


def detail(request):
    setting = ShopSetting.objects.get(pk=1)
    page = request.get_full_path()
    page = page.split('/')
    page = page[2]
    
    if page == 'product':
        page = 'Ürünler'
    else:
        page
    
    context = {
        'page': page,
        'setting': setting
    }
    return render(request, 'product/detail.html', context)


def cart(request):
    setting = ShopSetting.objects.get(pk=1)
    page = request.get_full_path()
    page = page.split('/')
    page = page[2]
    
    if page == 'product':
        page = 'Ürünler'
    else:
        page
    
    context = {
        'page': page,
        'setting': setting
    }
    return render(request, 'product/cart.html', context)


def checkout(request):
    setting = ShopSetting.objects.get(pk=1)
    page = request.get_full_path()
    page = page.split('/')
    page = page[2]
    
    if page == 'product':
        page = 'Ürünler'
    else:
        page
    
    context = {
        'page': page,
        'setting': setting
    }
    return render(request, 'product/checkout.html', context)