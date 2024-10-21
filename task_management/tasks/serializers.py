from rest_framework import serializers
from .models import (
    User,
    Task
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'mobile']
    
class TaskSerializer(serializers.ModelSerializer):
    assigned_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'created_at', 'task_type', 'completed_at', 'status', 'assigned_users']

class AssignTaskSerializer(serializers.Serializer):
    user_ids = serializers.ListField(
        child=serializers.IntegerField()
    )