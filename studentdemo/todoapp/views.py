from django.http import HttpResponse
from .models import Task
from django.shortcuts import render, redirect
from .forms import TaskForm
from django.views.decorators.http import require_POST
from django.http import JsonResponse

def index(request):
    # Fetch Data From Model
    tasks = Task.objects.all()

    # Fetch Form from Forms
    form = TaskForm()

    # Insert Model Data into Template, Run Template Code, an Return to Client
    return render(request, 'index.html', {'tasks': tasks, 'form': form})


@require_POST  # Ensure that only POST requests can access this view
def create_task(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        task = form.save()
        return JsonResponse({'status': 'ok', 'task_description': task.description, 'task_id': task.id})
    else:
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)