from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import TodoForm

from .models import Priority, TodoItem

# Create your views here.

def index(request):
    todos = TodoItem.objects.all()
    choices = Priority.objects.all()

    context = {
        "todos": todos,
        "form": TodoForm,
        "choices": choices
    }


    return render(request, 'todo/index.html', context)



def save_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo_item = TodoItem()
            todo_item.text = form.cleaned_data['text']
            priority = int(request.POST.get('priority'))
            todo_item.priority = Priority.objects.get(id=priority)

            todo_item.save()

            return redirect(reverse('todo:index'))
        else:
            return render(reverse, ('todo:index'))


    return redirect(reverse('todo:index'))