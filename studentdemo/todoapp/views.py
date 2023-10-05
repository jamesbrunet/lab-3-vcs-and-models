from django.http import HttpResponse
from .models import Task
from django.shortcuts import render
def index(request):
    # Fetch Data From Model
    tasks = Task.objects.all()

    # Insert Model Data into Template, Run Template Code, an Return to Client
    return render(request, 'index.html', {'tasks': tasks})

from .forms import TaskForm

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('some_view_name')  # Redirect to wherever you want after saving
    else:
        form = TaskForm()

    return render(request, 'template_name.html', {'form': form})