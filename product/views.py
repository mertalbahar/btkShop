from django.shortcuts import render
from .models import Product, ProductImages


def index(request):       
    products = Product.objects.all()
    
    context = {
        'products': products
    }
    return render(request, 'product/index.html', context)


def products_by_category(request, id):
    products = Product.objects.filter(category__id = id)
    
    context = {
        'products': products
    }
    
    return render(request, 'product/index.html', context)


def detail(request, id):
    product = Product.objects.get(pk=id)
    product_images = ProductImages.objects.filter(product = product)
    
    context = {
        'product': product,
        'images': product_images
    }
    return render(request, 'product/detail.html', context)


def cart(request):
    return render(request, 'product/cart.html')


def checkout(request):
    return render(request, 'product/checkout.html')