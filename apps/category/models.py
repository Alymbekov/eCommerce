
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', related_name='children', blank=True, null=True, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    def gen_slug(self):
        self.slug = self.title.lower() + "1"

    def save(self, *args, **kwargs):
        self.gen_slug()
        super().save(self, *args, **kwargs)

    def __str__(self):
        return self.title



