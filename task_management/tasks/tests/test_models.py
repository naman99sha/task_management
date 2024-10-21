from django.test import TestCase
from tasks.models import (
    User, 
    Task
)

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(name="John Doe", email="john@example.com", mobile="1234567890")

    def test_user_creation(self):
        self.assertEqual(self.user.name, "John Doe")
        self.assertEqual(self.user.email, "john@example.com")
        self.assertEqual(self.user.mobile, "1234567890")

class TaskModelTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(name="Task 1", description="This is a sample task.")

    def test_task_creation(self):
        self.assertEqual(self.task.name, "Task 1")
        self.assertEqual(self.task.description, "This is a sample task.")
        self.assertEqual(self.task.status, "Pending")
