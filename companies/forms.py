from django import forms
from .models import Company

class CompanyCreationForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['company_name', 'cnpj', 'address', 'cep', 'city', 'neighborhood', 'logo', 'bio']

        labels = {
            'company_name': ('Nome da empresa'),
            'cnpj': ('CNPJ da empresa'),
            'address': ('Endereço'),
            'cep': ('CEP'),
            'city': ('Cidade'),
            'neighborhood': ('Bairro'),
            'logo': ('Logo da sua empresa'),
            'bio': ('Descrição da empresa')
        }

    def __init__(self, *args, **kwargs):
        super(CompanyCreationForm, self).__init__(*args, **kwargs)
        self.fields['cep'].widget.attrs['placeholder'] = 'CEP'
        self.fields['company_name'].widget.attrs['placeholder'] = 'Insira aqui o nome da sua empresa'
        self.fields['cnpj'].widget.attrs['placeholder'] = 'Insira aqui o CNPJ da sua empresa'
        self.fields['address'].widget.attrs['placeholder'] = 'Insira aqui o endereço da sua empresa'
        self.fields['city'].widget.attrs['placeholder'] = 'Insira aqui a cidade da sua empresa'
        self.fields['neighborhood'].widget.attrs['placeholder'] = 'Insira aqui o bairro da sua empresa'
        self.fields['logo'].widget.attrs['placeholder'] = 'Insira aqui o logo da sua empresa'
        self.fields['bio'].widget.attrs['placeholder'] = 'Insira aqui uma breve descrição da empresa'

class CompanyEditForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['company_name', 'address', 'cep', 'city', 'neighborhood', 'logo', 'bio']

        labels = {
            'company_name': ('Nome da empresa'),
            'address': ('Endereço'),
            'cep': ('CEP'),
            'city': ('Cidade'),
            'neighborhood': ('Bairro'),
            'logo': ('Logo da sua empresa'),
            'bio': ('Descrição da empresa')
        }

    def __init__(self, *args, **kwargs):
        super(CompanyEditForm, self).__init__(*args, **kwargs)
        self.fields['cep'].widget.attrs['placeholder'] = 'CEP'
        self.fields['company_name'].widget.attrs['placeholder'] = 'Insira aqui o nome da empresa'
        self.fields['address'].widget.attrs['placeholder'] = 'Insira aqui o endereço da sua empresa'
        self.fields['city'].widget.attrs['placeholder'] = 'Insira aqui a cidade da sua empresa'
        self.fields['neighborhood'].widget.attrs['placeholder'] = 'Insira aqui o bairro da sua empresa'
        self.fields['logo'].widget.attrs['placeholder'] = 'Insira aqui o logo da sua empresa'
        self.fields['bio'].widget.attrs['placeholder'] = 'Insira aqui uma breve descrição da empresa'
