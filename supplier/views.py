from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from supplier.models import Supplier


class SupplierView(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = GetSupplierSerializer
    permission_classes = (permissions.IsAuthenticated,)


