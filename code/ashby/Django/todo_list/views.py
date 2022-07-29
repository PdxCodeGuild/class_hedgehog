from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone, dateformat


from .models import TodoItem
from .forms import TodoForm
# Create your views here.

#   todo_item:index

def index(request):
    todos = TodoItem.objects.all()
    form = TodoForm()
    context ={
        'todos': todos,
        'form': form,
    }

    return render(request, 'todo_list/index.html', context)


def detail(request, todo_id):
    try:
        todo= TodoItem.objects.get(id=todo_id)
    except TodoItem.DoesNotExist:
        return redirect(reverse('todo_list:index'))
   
    context = {'todo': todo}

    return render(request, 'todo_list/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('todo_list:index'))
        else:
            context = {'form': form,}
            return render(request, 'todo_list/index.html', context)

def delete(request, todo_id):
    try:
        todo= TodoItem.objects.get(id=todo_id)
    except TodoItem.DoesNotExist:
        return redirect(reverse('todo_list:index'))

    todo.delete()

    return redirect(reverse('todo_list:index'))

def complete(request, todo_id):
    try:
        todo= TodoItem.objects.get(id=todo_id)
    except TodoItem.DoesNotExist:
        return redirect(reverse('todo_list:index'))

    todo.completed_date = timezone.now()
    todo.save()
    return redirect(reverse('todo_list:index'))