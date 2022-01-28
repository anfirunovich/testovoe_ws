from rest_framework import routers

from customer import views

router = routers.DefaultRouter()
router.register('', views.CustomerViewSet, 'Customer')
router.register('purchase', views.PurchaseView, 'Purchase')
urlpatterns = router.urls
