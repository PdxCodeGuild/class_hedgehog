from django.shortcuts import render
from .models import User


def index(request):
    users = User.objects.all()

    context = {
        'users': users
    }

    return render(request, 'users/index.html', context)


def signup(request):
    return render(request, 'users/signup.html')
