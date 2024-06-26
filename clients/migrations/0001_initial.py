# Generated by Django 4.2.6 on 2023-10-29 19:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_cpf_cnpj.fields
import localflavor.br.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255)),
                ('cnpj', django_cpf_cnpj.fields.CNPJField(blank=True, max_length=18, null=True)),
                ('cpf', django_cpf_cnpj.fields.CPFField(blank=True, max_length=14, null=True)),
                ('email_primary', models.EmailField(blank=True, max_length=254, null=True)),
                ('email_secondary', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_primary', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('phone_secondary', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('address', models.CharField(max_length=255)),
                ('cep', localflavor.br.models.BRPostalCodeField(blank=True, max_length=9, null=True)),
                ('city', models.CharField(max_length=255)),
                ('neighborhood', models.CharField(max_length=255)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='user_files')),
                ('bio', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
