from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.car import CarViewSet
from .views.insurance import InsuranceViewSet
from .views.rent import RentViewSet


router = DefaultRouter()
router.register(r'cars', CarViewSet, base_name='car')
router.register(r'insurances', InsuranceViewSet, base_name='insurance')
router.register(r'rents', RentViewSet, base_name='rent-car')

urlpatterns = [
    path('', include(router.urls)),
]