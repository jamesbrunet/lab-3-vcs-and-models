from django.db import models
import datetime


class Task(models.Model):
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created_time = datetime.datetime.now()
    last_updated = datetime.datetime.now()

    def __str__(self):
        return self.description, self.created_time
