from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('iletisim', views.contact, name='contact'),
    path('hakkimizda', views.about, name='about'),
    path('referanslar', views.reference, name='reference'),
]