from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from carsshop.models import Carsshop, CarsOfCarsshop, Discount
from carsshop.serializers import GetPublicShowroom, GetCarsOfShowroom


class CarsshopPublicView(ModelViewSet):
    queryset = Carsshop.objects.all()
    serializer_class = GetPublicShowroom
    permission_classes = (permissions.AllowAny,)


class CarsshopView(ModelViewSet):
    queryset = CarsOfCarsshop.objects.all()
    serializer_class = GetCarsOfShowroom
    permission_classes = (permissions.IsAuthenticated,)


class DiscountViewSet(ModelViewSet):
    queryset = Discount.objects.filter(is_active=True)
    serializer_class = DiscountSerializer
    filterset_class = DiscountFilter