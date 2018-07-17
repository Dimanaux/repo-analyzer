from django.contrib.auth.models import User

from django.db import models


class TaskSet(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.IntegerField()

    title = models.CharField(max_length=120)
    description = models.TextField()

    time_from = models.DateTimeField(blank=True, null=True)
    time_to = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.title)


class Task(models.Model):
    task_set = models.ForeignKey(TaskSet, on_delete=models.CASCADE)
    number = models.IntegerField()

    title = models.CharField(max_length=120)
    description = models.TextField()

    time_from = models.DateTimeField()
    time_to = models.DateTimeField()

    def __str__(self):
        return str(self.title)
