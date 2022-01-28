from rest_framework import serializers

from carsshop.models import Carsshop, CarsOfCarsshop


class GetPublicShowroom(serializers.ModelSerializer):
    class Meta:
        model = Carsshop
        fields = ('title', 'description', 'address',)


class GetCarsOfShowroom(serializers.ModelSerializer):
    class Meta:
        model = CarsOfCarsshop
        fields = ('count', 'car', 'supplier',)