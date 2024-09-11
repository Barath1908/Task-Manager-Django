from django.http import Http404
from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm
from .task_manager import TaskManager


task_manager = TaskManager()

def home_view(request):
    priority = request.GET.get('priority',False)
    if priority:
        tasks = task_manager.filter_tasks_by_priority(priority)
    else:
        tasks = task_manager.view_all_tasks()

    context = {
        'tasks': tasks,
        'priority':priority,
    }
    return render(request, 'views/home_view.html', context )

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task_manager.add_task(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                priority=form.cleaned_data['priority'],
                status=form.cleaned_data['status']
            )
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'views/add_task.html', {'form': form})

def edit_task(request, task_id):
    try:
        task = task_manager.get_task_by_id(task_id)
        if request.method == 'POST':
            new_data = {
                'title': request.POST.get('title'),
                'description': request.POST.get('description'),
                'priority': request.POST.get('priority'),
                'status': request.POST.get('status')
            }
            task_manager.edit_task(task_id, new_data)
            
            return redirect('home')
        else:
            form = TaskForm(instance=task)
        return render(request, 'views/edit_task.html', {'form': form})
    except Task.DoesNotExist:
        raise Http404("Task does not exist")
    

def delete_task(request, task_id):
    try:
        task = task_manager.get_task_by_id(task_id)
        if request.method == 'POST':
            task_manager.delete_task(task_id)
            return redirect('home')
        return render(request, 'views/delete_task.html', {'task': task})
    except Task.DoesNotExist:
        raise Http404("Task does not exist")
    
    

    