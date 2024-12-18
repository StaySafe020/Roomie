"""
URL configuration for roomie_rental_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Roomieapp.views import UserRegistrationView, UserLoginView
from rest_framework import routers
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# Create a router and register your ViewSet with it



schema_view = get_schema_view(
    openapi.Info(
        title="user api",
        default_version='v1',
        description="API documentation for my project",
        terms_of_service="https://www.yourterms.com/",
        contact=openapi.Contact(email="jambongralpher@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.IsAuthenticatedOrReadOnly],
)
router = routers.DefaultRouter()
router.register(r'register', UserRegistrationView, basename='user-registration')
router.register('users/login', UserLoginView, basename='login')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('sample/', SampleView.as_view(), name='sample_view'),
    #path('roomie_rental_platform/login/', UserLoginView.as_view(), name='login'),

]
