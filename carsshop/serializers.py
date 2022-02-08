from rest_framework import serializers

from carsshop.models import Carsshop, CarsOfCarsshop, Discount


class GetPublicCarsshop(serializers.ModelSerializer):
    class Meta:
        model = Carsshop
        fields = ('title', 'description', 'address',)


class GetCarsOfCarsshop(serializers.ModelSerializer):
    class Meta:
        model = CarsOfCarsshop
        fields = ('count', 'car', 'supplier',)


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ('per')