from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import TodoForm

todos = []


def index(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo_text = request.POST.get("todo_text")
            priority = request.POST.get("priority")
            todos.append({
                "text": todo_text,
                "priority": priority,
                "completed": False
            })
        else:
            context = {
                "todos": todos,
                "form": form
            }
            return render(request, 'todos/index.html', context)

    context = {
        "todos": todos,
        "form": TodoForm()
    }

    return render(request, 'todos/index.html', context)


def delete_todo(request, index):
    if abs(index) >= len(todos):
        return HttpResponse("No")
    todos.pop(abs(index))
    return HttpResponseRedirect("/")


def complete_todo(request, index):
    index = abs(index)
    if index >= len(todos):
        return HttpResponse("No")
    todos[index]["completed"] = not todos[index]["completed"]
    return HttpResponseRedirect("/")
