from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from blog.models import BlogPost, User
from .forms import BlogForm


# Create your views here.

def loginPage(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
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


    context = {}
    return render(request, "blog/login_register.html", context)


def logoutUser(request):
    logout(request)
    return redirect('index')


def index(request):
    blogpost = BlogPost.objects.all()
    context = {
        "blogpost": blogpost
    }
    return render(request, 'blog/index.html', context)



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


def deletePost(request, pk):
    blogpost = BlogPost.objects.get(id=pk)
    if request.method == "POST":
        blogpost.delete()
        return redirect('index')
    return render(request, 'blog/delete.html', {'obj': blogpost})