from django.shortcuts import render
from django.views.generic import ListView, DetailView

from apps.category.models import Category


class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    fields = ['title', 'parent', ]
