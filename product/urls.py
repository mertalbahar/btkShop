from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='product'),
    path('detay', views.detail, name='detail'),
    path('sepet', views.cart, name='cart'),
    path('odeme', views.checkout, name='checkout'),
]