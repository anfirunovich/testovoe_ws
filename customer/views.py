from rest_framework import mixins, viewsets

from customer.models import Customer
from customer.serializers import CustomerSerializer


class SupplierViewSet(
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
