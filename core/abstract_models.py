from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CreatedAt(models.Model):
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UpdatedAt(models.Model):
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SoftDelete(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class AbstractDiscount(SoftDelete, CreatedAt, UpdatedAt):
    title = models.CharField(max_length=256, verbose_name='title')
    start = models.DateTimeField(verbose_name='start')
    end = models.DateTimeField(verbose_name='end')
    discount_percent = models.PositiveIntegerField(
        verbose_name='discount_percent',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100)
        ]
    )

    class Meta:
        abstract = True
