from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        'message': 'Hello you'
    }
    return render(request, 'greet/index.html', context)

def 
