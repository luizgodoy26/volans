from django.db import models
from django_cpf_cnpj.fields import CNPJField
from localflavor.br.models import BRPostalCodeField

class Company(models.Model):
    company_name = models.CharField(max_length=255)
    cnpj = CNPJField(masked=False)
    address = models.CharField(max_length=255)
    cep = BRPostalCodeField(null=True, blank=True)
    city = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='user_files', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.company_name