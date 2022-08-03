from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth

from .forms import AuthForm
from .models import TodoItem

def index(request):
    if request.user.is_anonymous:
        return redirect('login')
    todos = TodoItem.objects.filter(user=request.user)
    
    context = {
        "todos": todos
    }

    return render(request, 'todos/index.html', context)

def signup(request):
    if request.method == "POST":
        form = AuthForm(request.POST)
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
        'form': AuthForm()
    }
    return render(request, 'todos/signup.html', context)


def login(request):
    if request.method == "POST":
        form = AuthForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user != None:
               auth.login(request, user)
               return redirect('index')
        form.add_error(error="Invalid username or password", field="username")
        context = {
            "form": form
        }
        return render(request, 'todos/login.html', context)

    context = {
        "form": AuthForm()
    }
    return render(request, 'todos/login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('index')