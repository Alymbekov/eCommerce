from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from apps.category.models import Category
from .models import Product
from django.views.generic import ListView, CreateView, DetailView
from django.core.paginator import Paginator


def product_list(request):
    search_query = request.GET.get('search', '')
    categories = Category.objects.filter(parent=None).order_by('title')

    if search_query:
        product = Product.objects.filter(Q(p_name__icontains=search_query))
    else:
        product = Product.objects.all()
    paginator = Paginator(product, 3)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url,
        'categories': categories,
    }

    return render(request, 'products_list.html', context=context)



def index(request):
    return render(request, 'index.html', {})


"""class ProductListView(ListView):
    model = Product
    template_name = 'products_list.html'
    fields = ['p_name', 'price', 'category']
"""

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'




