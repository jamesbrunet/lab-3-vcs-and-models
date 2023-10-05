from django.db import models


class Task(models.Model):
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    updated_time = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description