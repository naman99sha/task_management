from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import (
    Task,
    User
)
from .serializers import (
    TaskSerializer,
    AssignTaskSerializer
)

@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def assign_task_to_users(request, task_id):
    task = Task.objects.get(pk=task_id)
    serializer = AssignTaskSerializer(data=request.data)
    if serializer.is_valid():
        user_ids = serializer.validated_data['user_ids']
        users = User.objects.filter(id__in=user_ids)
        if not users:
            return Response({'message': "Users mentioned doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)
        task.assigned_users.set(users)
        return Response({'message': 'Users assigned successfully!'})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_tasks_for_user(request, user_id):
    if User.objects.filter(pk=user_id):
        user = User.objects.get(pk=user_id)
        tasks = user.tasks.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)    
    return Response({'message': "User mentioned doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)