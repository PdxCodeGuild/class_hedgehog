from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from blog.models import BlogPost, User
from .forms import BlogForm


# Create your views here.

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username OR Password does not exist')

    context = {'page': page}

    return render(request, "blog/login_register.html", context)


def logoutUser(request):
    logout(request)
    return redirect('index')


def registerPage(request):
    # page = 'register'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "An error occurred during registration")

    return render(request, 'blog/login_register.html', {"form": form})



def index(request):
    blogpost = BlogPost.objects.all()
    context = {
        "blogpost": blogpost
    }
    return render(request, 'blog/index.html', context)


@login_required(login_url='login')
def createPost(request):
    form = BlogForm()
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        
            
    context = {
        "form": form
    }

    return render(request, 'blog/create_post.html', context)

@login_required(login_url='login')
def updatePost(request, pk):
    post = BlogPost.objects.get(id=pk)
    form = BlogForm(instance=post)

    if request.user != post.user:
        return HttpResponse("This is not your post!")



    if request.method == "POST":
        form = BlogForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'blog/create_post.html', context)

def deletePost(request, pk):
    blogpost = BlogPost.objects.get(id=pk)
    if request.method == "POST":
        blogpost.delete()
        return redirect('index')
    return render(request, 'blog/delete.html', {'obj': blogpost})