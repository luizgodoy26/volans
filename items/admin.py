from django.contrib import admin
from .models import Item, Size, Category, Stock

admin.site.register(Item)
admin.site.register(Size)
admin.site.register(Category)
admin.site.register(Stock)
