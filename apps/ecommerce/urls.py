from django.urls import  path
from apps.ecommerce.views import index

urlpatterns = [
    path('', index, name="index"),
]