from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='product'),
    path('sepet', views.cart, name='cart'),
    path('odeme', views.checkout, name='checkout'),
    path('kategori/<int:id>', views.products_by_category, name='products_by_category'),
    path('detay/<int:id>', views.detail, name='detail'),
]