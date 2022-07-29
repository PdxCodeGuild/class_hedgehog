
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import TodoItem, Priority
from .forms import TodoForm
import datetime



def index(request):
    todos = TodoItem.objects.all()
    priority_level = Priority.objects.all()

    context = {
        "todos": todos,
        "priority_level": priority_level,
        "form": TodoForm,
    }

    return render(request, 'todo/index.html', context)


def save_todo_item(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = TodoItem()
            todo.todo_item = form.cleaned_data['todo_item']
            priority = int(request.POST.get('priority'))
            todo.priority = Priority.objects.get(id=priority)

            todo.save()

            return redirect(reverse('todo:index'))

        else:
            return redirect(reverse('todo:index'))
    
    return redirect(reverse('todo:index'))

def completed(request, todo_id):
    try:
        todo = TodoItem.objects.get(id=todo_id)
    except TodoItem.DoesNotExist:
        return redirect(reverse('todo:index'))
    
    todo.completed_date = datetime.datetime.now()
    
    todo.save()
    return redirect(reverse('todo:index'))

def delete(request, todo_id):
    try:
        todo = TodoItem.objects.get(id=todo_id)
    except TodoItem.DoesNotExist:
        return redirect(reverse('todo:index'))

    todo.delete()

    return redirect(reverse('todo:index'))
