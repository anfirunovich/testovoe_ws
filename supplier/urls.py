from rest_framework import routers

from testovoe_ws.supplier import views


router = routers.DefaultRouter()
router.register('supplier', views.SupplierPublicView, 'Supplier')
urlpatterns = router.urls