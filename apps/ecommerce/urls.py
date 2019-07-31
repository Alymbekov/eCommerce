from django.urls import  path
from apps.ecommerce.views import *

urlpatterns = [
    path('', index, name="index"),
    path('products/', product_list, name='products_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]