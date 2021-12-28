from django.db import models


class Car(models.Model):
    model = models.CharField(max_length=256, verbose_name='model')
    color = models.CharField(max_length=256, verbose_name='color')
    year_of_release = models.DateTimeField()
    price = models.DecimalField()


