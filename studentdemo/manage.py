#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import datetime

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studentdemo.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)






class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.created_time = datetime.datetime.now()
        self.last_updated_time = self.created_time

    def update(self, new_title, new_description):
        self.title = new_title
        self.description = new_description
        self.last_updated_time = datetime.datetime.now()

# Example usage:
task = Task("Sample Task", "This is a sample task.")
print("Created Time:", task.created_time)
print("Last Updated Time:", task.last_updated_time)

# Update the task
task.update("Updated Task", "This task has been updated.")
print("Updated Time:", task.last_updated_time)

if __name__ == '__main__':
    main()
