
import datetime
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDoItem, Priority
from .forms import NewToDoForm

# Create your views here.
def index(request):
    todos = ToDoItem.objects.filter(completed_date__isnull=True)
    todos_comp = ToDoItem.objects.filter(completed_date__isnull=False)
    form = NewToDoForm(request.POST)

    context = {
        'todos': todos,
        'todos_comp': todos_comp,
        'form': form
    }

    return render(request, 'todo/index.html', context)

def save_todo_item(request):
    form = NewToDoForm(request.POST)
    if request.method == 'POST':
        todoitem = ToDoItem()
        if form.is_valid():
            todoitem.text = form.cleaned_data['text']
            todoitem.priority = form.cleaned_data['priority']
            if form.cleaned_data['completed_date']:
                todoitem.completed_date = form.cleaned_data['completed_date']
            
            todoitem.save()
            form = NewToDoForm()


            return redirect(reverse('todo:index'))
        else:
            return render(request, 'todo/index.html', context)

    context = {
        'form': NewToDoForm()
    }

    return render(request, 'todo/index.html', context)

def complete(request, todo_id):
    try:
        item = ToDoItem.objects.get(id=todo_id)
    except ToDoItem.DoesNotExist:
        return redirect(reverse('todo:index'))
    current_datetime = datetime.datetime.now()
    
    item.completed_date = current_datetime
    item.save()

    return redirect(reverse('todo:index'))

def delete(request, todo_id):
    try:
        item = ToDoItem.objects.get(id=todo_id)
        item.delete()
    except ToDoItem.DoesNotExist:
        return redirect(reverse('todo:index'))

    return redirect(reverse('todo:index'))

