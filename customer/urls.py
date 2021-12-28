from rest_framework import routers

from testovoe_ws.customer import views

router = routers.DefaultRouter()
router.register('', views.CustomerPrivateView, 'Customer')
urlpatterns = router.urls