from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import now
from .models import Todo, Tasks
from .forms import TaskForm, TodoForm


def home(request):
    todos = Todo.objects.all().order_by("-created_at")
    context = {
        "todos": todos
    }
    return render(request,"ToDo/home.html", context)

def todo_detail(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    tasks_var = Tasks.objects.filter(todo=todo)
    date = todo.created_at.strftime("%Y-%m-%d")

    context = {
        "todo": todo,
        "tasks": tasks_var,
        "date": date
    }

    return render(request, "ToDo/todo_detail.html", context)

def add_task(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.todo = todo
            task.save()

            return redirect("detail",todo_id=todo.id)
    else:
        form = TaskForm()

    context = {
        "todo": todo,
        "form": form,
    }

    return render(request, "ToDo/add_task.html", context)

def add_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("home")
        
    else:
        form = TodoForm()
    
    context = {
        "form" : form
    }

    return render(request, "ToDo/add_todo.html", context)

def delete_task(request, task_id, **kwatgs):
    task = get_object_or_404(Tasks, id=task_id)
    todo_id = task.todo.id

    if request.method == "POST":
        task.delete()

        return redirect("detail", todo_id=todo_id)
    
    return render(request, "ToDo/delete_task_confirm.html", {"task":task})

def task_completion(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)

    task.is_completed = not task.is_completed
    task.save()

    return redirect("detail", todo_id=task.todo.id)