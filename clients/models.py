from django.db import models
from django_cpf_cnpj.fields import CNPJField, CPFField
from phonenumber_field.modelfields import PhoneNumberField
from localflavor.br.models import BRPostalCodeField

from accounts.admin import User


class Client(models.Model):
    client_name = models.CharField(max_length=255)
    cnpj = CNPJField(masked=False, null=True, blank=True)
    cpf = CPFField(masked=False, null=True, blank=True)
    email_primary = models.EmailField(null=True, blank=True)
    email_secondary = models.EmailField(null=True, blank=True)
    phone_primary = PhoneNumberField(null=True, blank=True)
    phone_secondary = PhoneNumberField(null=True, blank=True)
    address = models.CharField(max_length=255)
    cep = BRPostalCodeField(null=True, blank=True)
    city = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='user_files', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.client_name