from django.urls import  path
from apps.ecommerce.views import *

urlpatterns = [
    path('', index, name="index"),
    path('products/', product_list, name='products_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/comment/', add_comment_to_product, name='add_comment'),

]