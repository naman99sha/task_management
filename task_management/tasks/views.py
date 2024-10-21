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

#View to create a task
@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    # If request body is valid
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # If request body is invalid
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#View to assign users to a task
@api_view(['POST'])
def assign_task_to_users(request, task_id):
    task = Task.objects.get(pk=task_id)
    serializer = AssignTaskSerializer(data=request.data)
    # If request body is in valid format
    if serializer.is_valid():
        user_ids = serializer.validated_data['user_ids']
        users = User.objects.filter(id__in=user_ids)
        # If no users with the mentioned IDs are found
        if not users:
            return Response({'message': "Users mentioned doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
        task.assigned_users.set(users)
        return Response({'message': 'Users assigned successfully!'})
    # If request body has an invalid format
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#View to get tasks assigned to a user
@api_view(['GET'])
def get_tasks_for_user(request, user_id):
    # If user exists
    if User.objects.filter(pk=user_id):
        user = User.objects.get(pk=user_id)
        tasks = user.tasks.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    # If user doesn't exist    
    return Response({'message': "User mentioned doesn't exist"}, status=status.HTTP_404_NOT_FOUND)