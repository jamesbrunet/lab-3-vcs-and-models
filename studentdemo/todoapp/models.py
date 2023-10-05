from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=255)

    @property
    def tasks(self):
        return Task.objects.filter(group=self)

class Task(models.Model):
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    updated_time = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.description