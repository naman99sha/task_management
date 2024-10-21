from django.db import models
from .enums.task_status_enum import TaskStatus

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(max_length=50, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=TaskStatus.choices(), default=TaskStatus.pending)
    assigned_users = models.ManyToManyField(User, related_name='tasks')

    def __str__(self):
        return self.name