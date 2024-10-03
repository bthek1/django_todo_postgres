from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ToDoForm
from .models import ToDo
from rest_framework import viewsets
from .serializers import ToDoSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from accounts.models import CustomUser

class ToDoViewSet(viewsets.ModelViewSet):
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # If the user is a superuser or staff, return all todos
        if self.request.user.is_superuser or self.request.user.is_staff:
            return ToDo.objects.all()
        # Otherwise, return only the todos for the current user
        return ToDo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]



@login_required
def add_todo(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save(user = request.user)
            return redirect('list_todo')  # Redirect to your todo list view
        else:
            # Add this to check for form validation errors
            print(form.errors)
    else:
        form = ToDoForm()

    return render(request, 'todos/add_todo.html', {'form': form})

@login_required
def todo_list(request):
    todos = ToDo.objects.filter(user=request.user)
    return render(request, 'todos/list_todo.html', {'todos': todos})
