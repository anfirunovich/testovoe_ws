from django.db import models

from core.abstract_models import AbstractDiscount, SoftDelete, UpdatedAt, CreatedAt
from supplier.models import Supplier


class Address(SoftDelete, UpdatedAt, CreatedAt):
    country = models.CharField(max_length=256, verbose_name='country')
    city = models.CharField(max_length=256, verbose_name='city')
    street = models.CharField(max_length=256, verbose_name='street')

    def __str__(self):
        return f'{self.city}, {self.country}, {self.street}'


class Carsshop(models.Model):
    title = models.CharField(max_length=256, verbose_name='title')
    description = models.TextField(max_length=256, verbose_name='description')
    address = models.OneToOneField(Address, null=True, on_delete=models.SET_NULL)
    year_of_foundation = models.DateTimeField(verbose_name='year_of_foundation')

    customers = models.ManyToManyField('customer.Customer', verbose_name='customers')
    cars = models.ManyToManyField(Supplier.Car, verbose_name='cars')


class CarsOfCarsshop(models.Model):
    count = models.PositiveIntegerField(default=1)
    car = models.ForeignKey(Supplier.Car, on_delete=models.SET_NULL, related_name='cars_of_carshop', null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='suppliers', null=True, blank=True)


class Discount(AbstractDiscount):
    cars = models.ManyToManyField(Carsshop, related_name='discounts')
    carsshop = models.ForeignKey(Carsshop, on_delete=models.CASCADE, related_name='discounts')
