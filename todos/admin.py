from django.contrib import admin
from .models import ToDo

class ToDoAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'completed', 'user']
    list_filter = ['completed', 'user']
    search_fields = ['title', 'description']

admin.site.register(ToDo, ToDoAdmin)
