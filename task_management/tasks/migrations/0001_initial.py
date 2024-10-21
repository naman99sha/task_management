# Generated by Django 5.1.2 on 2024-10-21 14:03

import tasks.enums.task_status_enum
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', models.CharField(blank=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('task_type', models.CharField(blank=True, max_length=50)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'pending'), ('Completed', 'completed')], default=tasks.enums.task_status_enum.TaskStatus['pending'], max_length=50)),
                ('assigned_users', models.ManyToManyField(related_name='tasks', to='tasks.user')),
            ],
        ),
    ]