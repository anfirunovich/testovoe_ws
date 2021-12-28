from django.db import models

from carsshop.models import Car


class Supplier(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    description = models.TextField(max_length=1000, verbose_name='description')
    year_of_foundation = models.DateTimeField(verbose_name='year_of_foundation')
    address = models.OneToOneField(null=True, on_delete=models.SET_NULL)

    cars = models.ManyToManyField(Car, verbose_name='SuppliersCar')
