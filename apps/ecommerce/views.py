from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, CreateView, DetailView
def index(request):
    return render(request, 'index.html', {})

class ProductListView(ListView):
    model = Product
    template_name = 'products_list.html'
    fields = ['p_name', 'price', 'category']

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
