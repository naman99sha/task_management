from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from tasks.models import (
    User, 
    Task
)

class TaskAPITest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create(name="John Doe", email="john@example.com")
        self.user2 = User.objects.create(name="Jane Doe", email="jane@example.com")
        self.task_data = {
            "name": "Task 1",
            "description": "This is a sample task"
        }

    def test_create_task(self):
        url = reverse('create-task')
        response = self.client.post(url, self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.task_data['name'])

    def test_assign_task_to_users(self):
        task = Task.objects.create(name="Task 1", description="Sample task")
        url = reverse('assign-task', kwargs={'task_id': task.id})
        data = {"user_ids": [self.user1.id, self.user2.id]}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.user1, task.assigned_users.all())
        self.assertIn(self.user2, task.assigned_users.all())

    def test_get_tasks_for_user(self):
        task = Task.objects.create(name="Task 1", description="Sample task")
        task.assigned_users.add(self.user1)
        url = reverse('user-tasks', kwargs={'user_id': self.user1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], task.name)
