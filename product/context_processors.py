from .models import Category
from home.models import ShopSetting


def categories(request):
    return {'categories': Category.objects.filter(parent = None)}

def setting(request):
    return {'setting': ShopSetting.objects.get(pk=1)}

def page(request):
    page = request.get_full_path()
    
    if page == '/':
        return {'page': 'Anasayfa'}
    
    elif page == '/product/':
        return {'page': 'Ürünler'}
    
    else:
        page = page.split('/')
        print(len(page))
        
        if len(page) > 2:
            return {'page': page[2]}
        else:
            return {'page': page[1]}