from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

# Set up the DRF router
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

# URL patterns for the account app
urlpatterns = [
    path('', include(router.urls)),  # Include the DRF router-generated URLs
]
