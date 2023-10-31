from django import forms
from .models import Client


class ClientCreationForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['client_name', 'cnpj', 'cpf', 'email_primary', 'email_secondary', 'phone_primary', 'phone_secondary', 'address', 'cep', 'city', 'neighborhood', 'logo', 'bio']

    def __init__(self, *args, **kwargs):
        super(ClientCreationForm, self).__init__(*args, **kwargs)
        self.fields['cep'].widget.attrs['placeholder'] = 'CEP'


class ClientEditForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['client_name', 'email_primary', 'email_secondary', 'phone_primary', 'phone_secondary', 'address', 'cep', 'city', 'neighborhood', 'logo', 'bio']

    def __init__(self, *args, **kwargs):
        super(ClientEditForm, self).__init__(*args, **kwargs)
        self.fields['cep'].widget.attrs['placeholder'] = 'CEP'
