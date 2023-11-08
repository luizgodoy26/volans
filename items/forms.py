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

"""
class ItemCreationForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'stock', 'unity', 'value', 'max_discount', 'description']

    def __init__(self, *args, **kwargs):
        super(ItemCreationForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Nome do item'


class ItemEditForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'stock', 'unity', 'value', 'max_discount', 'description']

    def __init__(self, *args, **kwargs):
        super(ItemEditForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Nome do item'
"""     