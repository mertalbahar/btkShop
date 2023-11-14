from django.shortcuts import render


def index(request):
    context = {
        'page': 'product'
    }
    return render(request, 'product/index.html', context)


def detail(request):
    context = {
        'page': 'detail'
    }
    return render(request, 'product/detail.html', context)


def cart(request):
    context = {
        'page': 'cart'
    }
    return render(request, 'product/cart.html', context)


def checkout(request):
    context = {
        'page': 'checkout'
    }
    return render(request, 'product/checkout.html', context)