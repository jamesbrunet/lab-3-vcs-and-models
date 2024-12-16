from django.db import models
import datetime

class Task(models.Model):
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created_time = models.DateField(default=datetime.now, blank=True)
    last_updated_time = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.description