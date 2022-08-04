from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .forms import AuthForm
# Create your views here.

@login_required
def profile(request):
    return render(request, 'blog/profile.html')

def register(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            auth.login(request, user)
            return render(request, 'blog/profile.html')
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
                return redirect('blog:profile')
        form.add_error(error="Invalid username or password", field="username")
        context = {
            "form": form
        }
        return render(request, 'blog/login.html', context)

    context = {
        "form": AuthForm()
    }
    return render(request, 'blog/login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('blog:login')