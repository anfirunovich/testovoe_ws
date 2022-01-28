from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from supplier.models import Supplier, Car


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = (
            'title',
            'year_of_foundation',
            'address',
            'cars'
        )


class GetSupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = (
            'title',
            'year_of_foundation',
            'address',
            'cars'
        )


class GetCarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = (
            "model",
            "year_of_release",
            "color",
            "price",
        )


class CarPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            'model',
            'price',
            )
