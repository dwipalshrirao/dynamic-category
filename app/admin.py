from django.contrib import admin

# Register your models here.
from .models import category,subcategory

admin.site.register(category)
admin.site.register(subcategory)