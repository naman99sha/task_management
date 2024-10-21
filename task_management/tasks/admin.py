from django.contrib import admin
from .models import (
    Task,
    User
)

class CustomAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
# Register your models here.
admin.site.register(Task, CustomAdmin)
admin.site.register(User, CustomAdmin)