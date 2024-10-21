from enum import Enum

class TaskStatus(Enum):
    pending = 'Pending'
    completed = 'Completed'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]