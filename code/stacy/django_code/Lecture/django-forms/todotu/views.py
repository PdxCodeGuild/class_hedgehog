from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import TodoForm

todos = [{
        "text": 'create todo list',
        "priority": 'high', 
        "completed": False
}]

def index(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo_text = request.POST.get("todo_text")
            print(todo_text)
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
    context = {
        "todos": todos,
        "form": TodoForm()
        }

    return render(request, 'todotu/index.html', context)

def delete_todo(request, index):
    index = abs(index)
    if index >= len(todos):
        return HttpResponse("Index does not exist")
    todos.pop(index)
    return HttpResponseRedirect("/")

def complete_todo(request, index):
    index = abs(index)
    if index >= len(todos):
        return HttpResponse("Index does not exist")
    todos[index]["completed"] = not todos[index]["completed"]
    return HttpResponseRedirect("/")
