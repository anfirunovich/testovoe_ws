from rest_framework import mixins, viewsets, permissions
from rest_framework.viewsets import ModelViewSet

from customer.models import Customer, Purchase
from customer.serializers import CustomerSerializer, GetPurchaseSerializer


class CustomerViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Customer.objects.all()

    default_serializer_class = CustomerSerializer
    serializer_class = CustomerSerializer


class PurchaseView(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = GetPurchaseSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_fields = ('car', 'car_showroom', 'discount',)
    search_fields = ('car', 'car_showroom', 'discount',)
