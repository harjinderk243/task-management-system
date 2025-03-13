from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

def home(request):
    return render(request, 'index.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

@login_required
def dashboard(request):
    if request.user.is_admin:
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'tasks': tasks})

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            messages.success(request, 'Task created successfully')
            return redirect('dashboard')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})

@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully')
            return redirect('dashboard')
    else:
        form = TaskForm(instance=task)
    return render(request, 'update_task.html', {'form': form, 'task': task})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully')
        return redirect('dashboard')
    return render(request, 'delete_task_confirm.html', {'task': task})

@login_required
def user_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out')
    return redirect('home')
