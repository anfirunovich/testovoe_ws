from django.db import models
from datetime import datetime


class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    last_name = models.CharField(max_length=100, verbose_name='last_name')
    email = models.EmailField(max_length=100, verbose_name='email')


class EmailVerification(models.Model):
    code = models.CharField(max_length=20, verbose_name='Проверочный код')
    email = models.EmailField(Customer)
    send_time = models.DateTimeField(datetime.now, null = True, blank = True)
    time = models.DateTimeField(null=True)
