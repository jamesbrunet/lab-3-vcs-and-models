from django.db import models

class Group(models.Model):
    groupName = models.CharField(max_length=100)
    numTasks = Task.

    @property
    def __tasks__(self):
        return self.numTasks


class Task(models.Model):
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


