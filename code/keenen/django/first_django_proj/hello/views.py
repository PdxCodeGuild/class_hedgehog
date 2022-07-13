from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    context = {
        'name': 'joe',
        "fruits": ['apple', 'banana', 'peach']
    }
    return render(request, 'hello/index.html', context)

def goodbye(request):
    return HttpResponse('Goodbye, World')

def hello(request, name):
    return HttpResponse(f'Hello, {name}')
