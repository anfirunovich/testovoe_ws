from django.db import models

class Car(models.Model):
    model = models.CharField(max_length=256, verbose_name='model')
    color = models.CharField(max_length=256, verbose_name='color')
    year_of_release = models.DateTimeField()
    price = models.DecimalField()


class Showroom(models.Model):
    title = models.CharField(max_length=256, verbose_name='title')
    description = models.TextField(max_length=256, verbose_name='description')
    address = models.OneToOneField(null=True, on_delete=models.SET_NULL)
    year_of_foundation = models.DateTimeField(verbose_name='year_of_foundation')

    customers = models.ManyToManyField('customer.Customer', verbose_name='customers')
    cars = models.ManyToManyField(Car, verbose_name='cars')





