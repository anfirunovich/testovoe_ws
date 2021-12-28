from rest_framework import serializers

from supplier.models import Supplier


class GetSupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = (
            "name",
            "description",
            "balance",
            "cars",
        )