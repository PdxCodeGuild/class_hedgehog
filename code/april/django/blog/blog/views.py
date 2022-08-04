
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from blog.forms import AuthForm


def index(request):
    return render(request, 'blog/index.html')


def register(request):
    if request.method == "POST":
        form = AuthForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            auth.login(request, user)
            return redirect('profile')
        else:
            context = {
                'form': form
            }
        return render(request, 'blog/register.html', context)
    context = {
        'form': AuthForm()
    }
    return render(request, 'blog/register.html', context)

def login(request):
    if request.method == "POST":
        form = AuthForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user != None:
                auth.login(request, user)
                next = request.GET.get('next')
                if next:
                    return redirect(next)
                return redirect('profile')
        form.add_error(error="Invalid username or password", field="username")
        context = {
            "form": form
        }
        return render(request, 'blog/login.html', context)

    context = {
        "form": AuthForm()
    }
    return render(request, 'blog/login.html', context)

@login_required
def profile(request):
    return render(request, 'blog/profile.html')

def logout(request):
    auth.logout(request)
    return redirect('index')