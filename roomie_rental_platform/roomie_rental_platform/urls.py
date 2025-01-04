from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Roomieapp.views import (
    UserRegistrationView,
    UserLoginView,
    UserProfileViewSet,
    PropertyListCreateView,
    PropertyDetailView,
)
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from Roomieapp import views
from Roomieapp.views import PropertyDetailViewSet, InquiryViewSet
# Schema view for API documentation
schema_view = get_schema_view(
    openapi.Info(
        title="User API",
        default_version='v1',
        description="API documentation for my project",
        contact=openapi.Contact(email="your_email@example.com"),
    ),
    public=True,
)

# Create a router and register your ViewSets
router = routers.DefaultRouter()
router.register(r'profiles', UserProfileViewSet, basename='userprofile')
router.register(r'properties', PropertyListCreateView, basename='property')
router.register(r'inquiries', InquiryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  # Include all registered routes from the router
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # User Registration and Login using class-based views
    path('api/register/', UserRegistrationView.as_view(), name='user-registration'),
    path('api/login/', UserLoginView.as_view(), name='user-login'),
    
]