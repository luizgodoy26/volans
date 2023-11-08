from django.db import models
from accounts.admin import User
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import *


class Item(models.Model):
    UNITS = (
        ('Unidade', 'Unidade'),
        ('Metros', 'Metros'),
        ('Quilos', 'Quilos'),
        ('Litros', 'Litros'),
        ('NA', 'NA'),
    )

    name = models.CharField(max_length=255)
    unity = models.CharField(max_length=10, choices=UNITS, default='NA')
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name



class Size(models.Model):
    size = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.size



class Category(models.Model):
    category = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.category



class Stock(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(Decimal('0.01'))])
    max_discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(Decimal('0.01')), MaxValueValidator(Decimal('100'))])
    