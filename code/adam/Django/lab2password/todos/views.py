from importlib.resources import contents
from django.shortcuts import redirect, render
from django.http import HttpResponse
# Create your views here.
def index(request):
    message = "Hello World"

    context = {
            "message": message
          }
    return render(request, "todos/index.html", context)