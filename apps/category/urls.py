from django.urls import path
from .views import *


urlpatterns = [
    path('categories/', CategoryListView.as_view(), name="categories"),
    path('categories/<str:slug>/', CategoryDetailView.as_view(), name="category_detail"),
]