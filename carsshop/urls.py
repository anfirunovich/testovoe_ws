from rest_framework import routers

from carsshop import views

router = routers.DefaultRouter()
router.register('', views.CarsshopPublicView, 'Carsshop')
router.register('cars_of_showroom', views.CarsshopView, 'CarsOfShowroom')
urlpatterns = router.urls
