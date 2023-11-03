from django.db import models
from accounts.admin import User

class Item(models.Model):
    UNITS = (
        ('Unidade', 'Unidade'),
        ('Metros', 'Metros'),
        ('Quilos', 'Quilos'),
        ('Litros', 'Litros'),
        ('NA', 'NA'),
    )

    name = models.CharField(max_length=255)
    stock = models.PositiveIntegerField(null=True, blank=True)
    unity = models.CharField(max_length=10, choices=UNITS, null=True, blank=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    max_discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
