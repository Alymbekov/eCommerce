from django.db import models
from apps.category.models import Category

class Product(models.Model):
    p_name = models.CharField(max_length=100, verbose_name='Наименование продукта')
    description = models.TextField(verbose_name='Характеристики')
    #features = models.ForeignKey()
    price = models.PositiveIntegerField(verbose_name='Цена')
    category = models.ForeignKey(Category, verbose_name='Категория',on_delete=models.CASCADE, related_name='products')
    stock = models.PositiveSmallIntegerField(verbose_name='Количество')
    created_ad = models.DateField(auto_now_add=True, verbose_name='Дата добавления:')
    updated_ad = models.DateField(auto_now_add=True, verbose_name='Дата обновления:')
    artikul = models.CharField(max_length=100, verbose_name='Код товара')
    slug = models.SlugField()
    image = models.ImageField(upload_to='media/products/', verbose_name='Фото товара')
    #comment = models.ForeignKey()

    def __str__(self):
        return self.p_name
