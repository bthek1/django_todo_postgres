from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from account.views import UserViewSet
from todos.views import ToDoViewSet
from rest_framework.authtoken import views


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'todos', ToDoViewSet, basename='todo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('accounts/', include('django.contrib.auth.urls')),  # Add this line for auth views
]