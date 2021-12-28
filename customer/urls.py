from rest_framework import routers

from customer.models import Customer

router = routers.DefaultRouter()
router.register('Customer', Customer.ViewSet)
urlpatterns = router.urls