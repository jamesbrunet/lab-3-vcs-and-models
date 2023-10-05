from django.db import models


class Task(models.Model):
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    updated_time = models.DateTimeField()
    created_time = models.DateTimeField()

    def __str__(self):
        return self.description