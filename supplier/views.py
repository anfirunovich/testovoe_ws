from rest_framework import mixins, viewsets

from supplier.models import Supplier
from supplier.serializers import SupplierSerializer


class SupplierViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Supplier.objects.all()

    default_serializer_class = SupplierSerializer
    serializer_class = SupplierSerializer

