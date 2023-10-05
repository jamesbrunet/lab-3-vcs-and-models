from django.db import models


class Task(models.Model):
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created_time = models.TimeField(auto_now_add=True)
    last_updated_time = models.TimeField(auto_now=True)

class Group(models.Model):
    name = models.CharField(max_length=255)
    task = models.CharField(max_length=255)

    @property
    def taskNumber(self):



    def __str__(self):
        return self.description