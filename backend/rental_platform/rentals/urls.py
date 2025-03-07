# filepath: /rental-platform-backend/rentals/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LandlordViewSet, TenantViewSet, PropertyViewSet, RentalViewSet

router = DefaultRouter()
router.register(r'landlords', LandlordViewSet)
router.register(r'tenants', TenantViewSet)
router.register(r'properties', PropertyViewSet)
router.register(r'rentals', RentalViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]