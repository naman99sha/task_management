from django.urls import path
from .views import (
    create_task, 
    assign_task_to_users, 
    get_tasks_for_user
)

urlpatterns = [
    path('tasks/create/', create_task, name='create-task'),
    path('tasks/<int:task_id>/assign/', assign_task_to_users, name='assign-task'),
    path('users/<int:user_id>/tasks/', get_tasks_for_user, name='user-tasks'),
]
