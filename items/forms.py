from django import forms
from .models import Item, Size, Category, Stock

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'unity', 'description']

class SizeForm(forms.ModelForm):
    class Meta:
        model = Size
        fields = ['size']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['item', 'size', 'category', 'quantity', 'price', 'max_discount']

