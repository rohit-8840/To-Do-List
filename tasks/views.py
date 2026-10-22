from django.shortcuts import get_object_or_404, redirect, render
from .forms import TaskForm
from .models import Task

def task_list(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm()

    tasks = Task.objects.all()
    return render(request, "tasks/task_list.html", {
        "form": form,
        "tasks": tasks,
        "remaining_count": tasks.filter(completed=False).count(),
        "completed_count": tasks.filter(completed=True).count(),
    })

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.completed = not task.completed
        task.save(update_fields=["completed"])
    return redirect("task_list")

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/edit_task.html", {"form": form, "task": task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
    return redirect("task_list")
