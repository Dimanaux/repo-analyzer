from django.contrib import admin

from front.models import (
    Task,
    TaskSet,
)

admin.register(Task)
admin.register(TaskSet)
