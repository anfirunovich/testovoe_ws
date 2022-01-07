from django.db import models

from supplier.models import Supplier, Car


class Carsshop(models.Model):
    title = models.CharField(max_length=256, verbose_name='title')
    description = models.TextField(max_length=256, verbose_name='description')
    address = models.OneToOneField(null=True, on_delete=models.SET_NULL)
    year_of_foundation = models.DateTimeField(verbose_name='year_of_foundation')

    customers = models.ManyToManyField('customer.Customer', verbose_name='customers')
    cars = models.ManyToManyField(Supplier.Car, verbose_name='cars')


class CarsOfCarsshop(models.Model):
    count = models.PositiveIntegerField(default=1)
    car = models.ForeignKey(Car,on_delete=models.SET_NULL, related_name='cars_of_carshop', null=True)
    car_showroom = models.ForeignKey(Carsshop, on_delete=models.CASCADE, related_name='carsshop', null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='suppliers', null=True, blank=True)


