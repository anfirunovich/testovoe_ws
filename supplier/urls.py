from rest_framework import routers

from supplier.views import SupplierViewSet


router = routers.DefaultRouter()
router.register('supplier', SupplierViewSet)
urlpatterns = router.urls