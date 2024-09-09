from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site
    path('api-auth/', include('rest_framework.urls')),  # DRF browsable API login/logout
    path('api-token-auth/', views.obtain_auth_token),  # Token authentication endpoint
    path('accounts/', include('allauth.urls')),  # Add this line for allauth
    path("", include("pages.urls")),
    path('todos/', include('todos.urls')),  # Include URLs from the todos app
]
