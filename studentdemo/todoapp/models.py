from django.db import models


class Task(models.Model):
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    #created_time = models.TimeField(blank=True)
    #last_updated_time = models.TimeField(blank=True)

    def __str__(self):
        return self.description