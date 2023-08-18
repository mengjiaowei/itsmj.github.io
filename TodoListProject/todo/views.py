from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        Task.objects.create(title=title)
        return redirect('task_list')
    return render(request, 'todo/task_form.html')

def task_update(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.save()
        return redirect('task_list')
    return render(request, 'todo/task_form.html', {'task': task})

def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'todo/task_confirm_delete.html', {'task': task})
