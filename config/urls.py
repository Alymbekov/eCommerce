
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ecommerce/', include('apps.ecommerce.urls')),
    path('admin/', admin.site.urls),
]
