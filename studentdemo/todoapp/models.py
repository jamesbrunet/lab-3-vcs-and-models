from django.db import models
from django.conf import settings
from django.utils import timezone


class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()

    def __str__(self):
        return self.description

    @property
    def due_today(self):
        return self.due_date >= timezone.now() - timezone.timedelta(days=1)