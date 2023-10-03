from django.http import HttpResponse
from .models import Task
from django.shortcuts import render
def index(request):
    # Fetch Data From Model
    tasks = Task.objects.all()

    # Insert Model Data into Template, Run Template Code, an Return to Client
    return render(request, 'index.html', {'tasks': tasks})
