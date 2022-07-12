from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        "name": "Joe",
        "fruits": ["Kiwi","Banana","Apple"]
    }
    return render(request, 'hello/index.html', context)

def goodbye(request):
    return HttpResponse('Goodbye!')

def hello(request, name):
    return HttpResponse(f'Hello, {name}')

