from django import forms
from .models import Item

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