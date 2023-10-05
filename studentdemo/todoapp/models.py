from django.db import models
from django.utils import timezone


class Task(models.Model):
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created_time = models.DateTimeField(default=timezone.now)
    last_updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description