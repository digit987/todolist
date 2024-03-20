from django.shortcuts import render, redirect
from .models import Task

def todo_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        task_name = request.POST['task_name']
        Task.objects.create(task_name=task_name)
        return redirect('todo_list')
    return render(request, 'add_task.html')

def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('todo_list')

def mark_completed(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completed = True
    task.save()
    return redirect('todo_list')
