from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.db.models.functions import Now
from .models import Priority, TodoItem

def index(request):
    all_todo_items = TodoItem.objects.all().order_by('-id')

    context = {
        'all_todo_items': all_todo_items
    }
    return render(request, 'index.html', context) 

def save_todo_item(request):
    form = request.POST

    todo_text = form['todo_text']
    todo_priority = form['todo_priority']
    
    todo_priority, create = Priority.objects.get_or_create(priority=todo_priority)
    TodoItem.objects.create(todo_text=todo_text, todo_priority=todo_priority)    

    all_todo_items = TodoItem.objects.all().order_by('-id')

    context = {
        'all_todo_items': all_todo_items
    }

    return render(request, 'index.html', context)

def complete_todo_item(request, todo_id):

    todo_item = get_object_or_404(TodoItem, id=todo_id)
    todo_item.completed_date = Now()
    todo_item.save()

    all_todo_items = TodoItem.objects.all().order_by('-id')
    context = {
        'all_todo_items': all_todo_items
    }
    return render(request, 'index.html', context) 

def delete_todo_item(request, todo_id):
    
    todo_item = get_object_or_404(TodoItem, id=todo_id)
    todo_item.delete()

    all_todo_items = TodoItem.objects.all().order_by('-id')
    context = {
        'all_todo_items': all_todo_items
    }
    return render(request, 'index.html', context) 