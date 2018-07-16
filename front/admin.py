from django.contrib import admin

from front.models import (
    Task,
    TaskSet,
)

admin.site.register(Task)
admin.site.register(TaskSet)
