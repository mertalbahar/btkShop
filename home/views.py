from django.shortcuts import render


def index(request):
    context = {
        'page': 'home'
    }
    return render(request, 'home/index.html', context)


def contact(request):
    context = {
        'page': 'contact'
    }
    return render(request, 'home/contact.html', context)


def about(request):
    context = {
        'page': 'about'
    }
    return render(request, 'home/about.html', context)


def reference(request):
    context = {
        'page': 'reference'
    }
    return render(request, 'home/reference.html', context)