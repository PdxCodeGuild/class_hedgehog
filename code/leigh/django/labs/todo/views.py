
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import TodoItem, Priority
from .forms import NewTodoForm
import datetime

def index(request):
    todos = TodoItem.objects.all()
    priorities = Priority.objects.all()

    context = {
        "todos": todos,
        "form": NewTodoForm,
        "priorities": priorities
    }
    return render(request, "todo/index.html", context)

def save_todo_item(request):
    if request.method == "POST":
        form = NewTodoForm(request.POST)
        if form.is_valid():
            todo = TodoItem()
            todo.description = form.cleaned_data['description']
            priority_id = int(request.POST.get("priority"))
            todo.priority = Priority.objects.get(id=priority_id)
            
            todo.save()

            return redirect(reverse('todo:index'))
        else:
            return redirect(reverse('todo:index'))
    
    return redirect(reverse('todo:index'))

    
def complete(request, todo_id):
    try:
        grocery_item = TodoItem.objects.get(id=todo_id)
    except TodoItem.DoesNotExist:
        return redirect(reverse('todo:index'))
    
    grocery_item.completed_date = datetime.datetime.now()
    
    grocery_item.save()
    return redirect(reverse("todo:index"))


def delete(request, todo_id):
    try:
        grocery_item = TodoItem.objects.get(id=todo_id)
    except TodoItem.DoesNotExist:
        return redirect(reverse('todo:index'))
    
    grocery_item.delete()
    return redirect(reverse('todo:index'))