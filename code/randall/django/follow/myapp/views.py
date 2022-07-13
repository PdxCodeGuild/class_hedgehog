from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')

def hello(request, name):
    return HttpResponse(f"Hello, " + name + ".")