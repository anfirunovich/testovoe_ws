from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    last_name = models.CharField(max_length=100, verbose_name='last_name')
    email = models.EmailField(max_length=100, verbose_name='email')

