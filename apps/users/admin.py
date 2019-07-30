from django.contrib import admin
from apps.users.models import User, Profile

admin.site.register(User)
admin.site.register(Profile)