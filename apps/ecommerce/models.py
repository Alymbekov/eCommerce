import os

from django.db import models
from django.utils.crypto import random

from apps.category.models import Category
from apps.users.models import User


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 3934343433)
    name, ext = get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f'product_images/{new_filename}/{final_filename}'


class Product(models.Model):
    p_name = models.CharField(max_length=100, verbose_name='Наименование продукта')
    description = models.TextField(verbose_name='Характеристики')
    #features = models.ForeignKey()
    price = models.PositiveIntegerField(verbose_name='Цена')
    category = models.ForeignKey(Category,
                                 verbose_name='Категория',
                                 on_delete=models.CASCADE,
                                 related_name='products',
                                 blank=True,
                                 null=True,
                                 )
    stock = models.PositiveSmallIntegerField(verbose_name='Количество')
    created_ad = models.DateField(auto_now_add=True, verbose_name='Дата добавления:')
    updated_ad = models.DateField(auto_now_add=True, verbose_name='Дата обновления:')
    artikul = models.CharField(max_length=100, verbose_name='Код товара')
    slug = models.SlugField(null=True, blank=True)
    #image = models.ImageField(upload_to='media/products/', verbose_name='Фото товара')
    #comment = models.ForeignKey()

    def gen_slug(self):
        self.slug = self.p_name.lower() + "1"

    def save(self, *args, **kwargs):
        self.gen_slug()
        super().save(self, *args, **kwargs)

    def __str__(self):
        return self.p_name


class ProductImage(models.Model):
    image = models.ImageField(upload_to=upload_image_path)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name="images")

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.product.p_name}.jpg'


class Comment(models.Model):
    post = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment



