from django.urls import path

from mainapp.views import index, contacts, product, about, products

app_name = 'mainapp'

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product/', product, name='product'),
    path('products/', products, name='products'),
    path('about/', about, name='about'),
]
