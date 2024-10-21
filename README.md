# Django Task Management API

A task management system built using **Django** and **Django Rest Framework** (DRF) that allows users to create tasks, assign tasks to users, and retrieve tasks assigned to specific users.

## Features

- **Create Task**: Create tasks with a name and description.
- **Assign Task**: Assign tasks to one or more users.
- **Retrieve User's Tasks**: Fetch all tasks assigned to a specific user.
- **Unit Tests**: Includes test cases for models, views, and services.

---

## Project Structure

```bash
task_management/
    ├── manage.py
    ├── task_management/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── tasks/
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── migrations/
        │   └── __init__.py
        ├── models.py
        ├── serializers.py
        ├── views.py
        ├── urls.py
        ├── tests/
        │   ├── __init__.py
        │   ├── test_models.py
        │   ├── test_views.py
```

# Prerequisites

Ensure that you have the following installed:

- **Python 3.8+**
- **Django 4.0+**
- **Django Rest Framework**
- **SQLite3** (default)
- **Virtual environment** (recommended)

---

# Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/django-task-management-api.git
cd django-task-management-api
```

### 2. Create a Virtual Environment
It is recommended to create a virtual environment to manage dependencies.

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations
```bash
python manage.py migrate
```

### 5. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6. Run Development Server
```bash
python manage.py runserver
```
The server will be running at http://127.0.0.1:8000/

# API Endpoints

The Task Management API provides the following endpoints:

### 1. Create a Task

- **URL**: `/api/tasks/create/`
- **Method**: `POST`
- **Description**: Creates a new task.
- **Payload Example**:

```json
{
  "name": "Sample Task",
  "description": "This is a sample task."
}
```

### 2. Assign a Task to Users
- **URL**: `/api/tasks/<task_id>/assign/`
- **Method**: `POST`
- **Description**: Assigns a task to one or more users.
- **Payload Example**:

```json
{
  "user_ids": [1, 2, 3]
}
```

### 3. Retrieve Tasks for a Specific User
- **URL**: `/api/users/<user_id>/tasks/`
- **Method**: `GET`
- **Description**: Retrieves all tasks assigned to a specific user.

## Example Request

### Create a task

```bash
curl -X POST http://127.0.0.1:8000/api/tasks/create/ \
-H 'Content-Type: application/json' \
-d '{"name": "Test Task", "description": "Task description"}'
```

### Assign a task
```bash
curl -X POST http://127.0.0.1:8000/api/tasks/1/assign/ \
-H 'Content-Type: application/json' \
-d '{"user_ids": [1, 2]}'
```

## Unit tests
Unit tests are available for models, views, and services to ensure the correctness of the application.

### Running Unit tests
To run all the tests, simply execute:

```bash
python manage.py test tasks.tests
```

### Test Structure
Tests are organized in the `tests/` directory inside the `tasks` app. This directory includes:

- `test_models.py`: Tests for the task and user models.
- `test_views.py`: Tests for the API views.
- `test_services.py`: Tests for the business logic encapsulated in services.
