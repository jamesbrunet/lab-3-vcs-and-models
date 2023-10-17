from django.test import TestCase

import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Task


class TaskModelTests(TestCase):
    def test_should_not_be_due_soon_if_overdue(self):
        """
        due_soon() returns False for overdue tasks
        """
        past_time = timezone.now() - datetime.timedelta(days=30)
        task = Task(description='I should have definitely done this', due_date=past_time)
        self.assertIs(task.due_soon, False)

    def test_should_not_be_due_soon_if_due_far_in_future(self):
        """
        due_soon() returns False for tasks far in far future
        """
        future_time = timezone.now() + datetime.timedelta(days=30)
        task = Task(description='Save for retirement', due_date=future_time)
        self.assertIs(task.due_soon, False)

    def test_should_be_due_soon(self):
        """
        due_soon() returns False for tasks due soon
        """
        contemporary_time = timezone.now() + datetime.timedelta(hours=2)
        task = Task(description='Do the dishes', due_date=contemporary_time)
        self.assertIs(task.due_soon, True)