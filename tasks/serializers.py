from rest_framework import serializers
from .models import Task, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'color']

class TaskSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True, required=False, allow_null=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'priority', 'due_date', 'category', 'category_id', 'created_at', 'updated_at', 'completed_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
