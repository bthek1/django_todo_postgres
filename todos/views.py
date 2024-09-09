from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ToDoForm
from .models import ToDo
from rest_framework import viewsets
from .serializers import ToDoSerializer
from rest_framework.permissions import IsAuthenticated


class ToDoViewSet(viewsets.ModelViewSet):
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

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
