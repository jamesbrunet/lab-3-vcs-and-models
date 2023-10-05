from django.db import models

class Group(models.Model):
    groupName = models.CharField(max_length=100)

    @property
    def numTasks(self):
        return Task.objects.filter(group=self)


class Task(models.Model):
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


