from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from datetime import datetime

from carsshop.models import Car, Carsshop
from core.abstract_models import CreatedAt, UpdatedAt, SoftDelete


class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    last_name = models.CharField(max_length=100, verbose_name='last_name')
    email = models.EmailField(max_length=100, verbose_name='email')


class Purchase(CreatedAt, UpdatedAt, SoftDelete):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, to_field='vin', on_delete=models.SET_NULL, related_name='cars', null=True, blank=True)
    count = models.PositiveIntegerField(default=1)
    carsshop = models.ForeignKey(Carsshop, on_delete=models.SET_NULL, related_name='carsshop', null=True, blank=True)
    discount = models.IntegerField(
        validators=(MinValueValidator(1),
                    MaxValueValidator(100),
                    )
    )


class EmailVerification(models.Model):
    code = models.CharField(max_length=20, verbose_name='Проверочный код')
    email = models.EmailField(Customer)
    send_time = models.DateTimeField(datetime.now, null=True, blank=True)
    time = models.DateTimeField(null=True)