from django.shortcuts import render, redirect
from .models import User
from django.urls import reverse
from django.contrib import auth
# Create your views here.
def index(request):
    users = User.objects.all()

    context = {
        'users': users
    }

    return render(request, 'users/index.html', context)

def signup(request):
    if request.method == 'POST':
       User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
       return redirect('users:login')
    return render(request, 'users/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('users:index')

    return render(request, 'users/login.html')

def logout(request):
    auth.logout(request)
    return redirect('users:index')