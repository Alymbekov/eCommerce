from django.contrib import admin
from .models import Product, ProductImage
from import_export import resources
from import_export.admin import ImportExportModelAdmin

@admin.register(Product)
class PersonAdmin(ImportExportModelAdmin):
    pass

admin.site.register(ProductImage)