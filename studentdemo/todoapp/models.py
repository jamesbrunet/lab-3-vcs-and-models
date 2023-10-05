from django.db import models
from datetime import datetime

class Task(models.Model):
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created_time = datetime.now()
    last_updated_time = datetime.now()

    def __str__(self):
        return self.description