from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ToDoViewSet, UserViewSet, add_todo, todo_list

# Set up the DRF router
router = DefaultRouter()
router.register(r'todos', ToDoViewSet, basename='todo')  # Explicitly specify the basename
router.register(r'users', UserViewSet, basename='user')  # Explicitly specify the basename

# URL patterns for the todos app
urlpatterns = [
    path('add/', add_todo, name='add_todo'),  # URL for the form view to add a new todo
    path('list/', todo_list, name='list_todo'),  # URL for the list view to display todos
    path('', include(router.urls)),  # Include the DRF router-generated URLs
]
