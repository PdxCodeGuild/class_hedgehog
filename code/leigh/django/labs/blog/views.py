from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .forms import AuthForm, NewPost
from .models import BlogPost
from django.utils import timezone

# Create your views here.
def register(request):
    if request.method == "POST":
        form = AuthForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            auth.login(request, user)
            return redirect('blog:profile')
    context = {
        'form': AuthForm(),
    }
    return render(request, 'blog/register.html', context)

def login(request):
    if request.method == "POST":
        form = AuthForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                next = request.GET.get('next')
                if next:
                    return redirect(next)
                return redirect('blog:profile')
        form.add_error(error="Invalid username or password", field="username")
        context = {
            "form": form
        }
    else:
        context = {
            "form": AuthForm()
        }
    return render(request, 'blog/login.html', context)

def profile(request):
    if request.user.is_anonymous:
        return redirect('blog:login')
    posts = BlogPost.objects.filter(user=request.user)
    context = {
        "posts": posts
    }
    return render(request, 'blog/profile.html', context)

def create(request):
    if request.user.is_anonymous:
        return redirect('blog:login')
    if request.method == "POST":
        form = NewPost(request.POST)
        if form.is_valid():
            post = BlogPost()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.user = request.user
            post.public = form.cleaned_data['public']
            post.image = form.cleaned_data['image']
            post.save()
        return redirect('blog:profile')
    context = {
        'form': NewPost
    }
    return render(request, 'blog/create.html', context)

def logout(request):
    auth.logout(request)
    return redirect('blog:login')

def edit(request, post_id):
    if request.user.is_anonymous:
        return redirect('blog:login')
    if request.method == "GET":
        try:
            post = BlogPost.objects.get(id=post_id)
        except BlogPost.DoesNotExist:
            return redirect('blog:profile')
        if request.user == post.user:
            context = {
                "post": post,
                "form": NewPost({"title": post.title, "body": post.body, "public": post.public, "image": post.image})
            }
            return render(request, 'blog/edit.html', context)
        else:
            return redirect('blog:profile')
    elif request.method == "POST":
        try:
            post = BlogPost.objects.get(id=post_id)
        except BlogPost.DoesNotExist:
            return redirect('blog:profile')
        if request.user == post.user:
            form = NewPost(request.POST)
            if form.is_valid():
                post.title = form.cleaned_data['title']
                post.body = form.cleaned_data['body']
                post.public = form.cleaned_data['public']
                post.image = form.cleaned_data['image']
                post.save()
            return redirect('blog:profile')
    return redirect('blog:profile')

def posts(request):
    if request.user.is_anonymous:
        return redirect('blog:login')
    posts = BlogPost.objects.filter(public=True)
    context = {
        "posts": posts
    }
    return render(request, 'blog/posts.html', context)

def post_detail(request, post_id):
    if request.user.is_anonymous:
        return redirect('blog:login')
    post = BlogPost.objects.get(id=post_id)
    context = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', context)