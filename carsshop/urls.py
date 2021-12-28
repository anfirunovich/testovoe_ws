from rest_framework import routers

from testovoe_ws.carsshop import views

router = routers.DefaultRouter()
router.register('', views.CustomerPrivateView, 'Carsshop')
urlpatterns = router.urls