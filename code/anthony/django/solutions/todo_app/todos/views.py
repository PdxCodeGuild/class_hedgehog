from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth

from .forms import SignupForm
from .models import TodoItem

def index(request):
    todos = TodoItem.objects.filter(user=request.user)
    
    context = {
        "todos": todos
    }

    return render(request, 'todos/index.html', context)

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            auth.login(request, user)
            return render(request, 'todos/signup.html')
        else:
            context = {
                'form': form
            }
            return render(request, 'todos/signup.html', context)


    context = {
        'form': SignupForm()
    }
    return render(request, 'todos/signup.html', context)
