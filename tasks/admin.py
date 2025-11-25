from django.contrib import admin
from .models import Task, Category

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'status', 'priority', 'due_date', 'created_at')
    list_filter = ('status', 'priority')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'created_at')
