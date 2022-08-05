from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .forms import AuthForm, NewPost
from .models import BlogPost
from django.urls import reverse
# Create your views here.

def index(request):
    post = BlogPost.objects.all()
    context = {
        'posts': post
    }
    return render(request, 'blog/index.html', context)


@login_required
def profile(request):
    form = NewPost(request.POST)
    post = BlogPost.objects.filter(user=request.user)
    context = {
        'form': form,
        'posts': post
    }
    return render(request, 'blog/profile.html', context)

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

@login_required
def create_post(request):
    form = NewPost(request.POST, request.FILES)
    if request.method == "POST":
        blog_post = BlogPost()
        if form.is_valid():
            blog_post.title = form.cleaned_data['title']
            blog_post.body = form.cleaned_data['body']
            blog_post.image = form.cleaned_data['image']
            blog_post.user = request.user
            if form.cleaned_data['public']:
                blog_post.public = True
            else:
                blog_post.public = False
            
            blog_post.save()
            form = NewPost()
        
            return redirect(reverse('blog:profile'))
        else:
            return render(request, 'blog/profile.html', context)
    context = {
        'form': NewPost()
    }

    return render(request, 'blog/profile.html', context)

@login_required
def editpost(request, post_id):
    if request.method == "GET":
        try:
            post = BlogPost.objects.get(id=post_id, user=request.user)
        except BlogPost.DoesNotExist:
            return redirect('blog:profile')
        context = {
            "post": post,
            'form': NewPost({"title": post.title, 'body': post.body, 'public': post.public, 'image': post.image})
        }
        return render(request, 'blog/edit.html', context)
    elif request.method == 'POST':
        try:
            post = BlogPost.objects.get(id=post_id)
        except BlogPost.DoesNotExist:
            return redirect('blog:profile')

        form = NewPost(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            if form.cleaned_data['public']:
                post.public = True
            else:
                post.public = False
            post.save()
        return redirect('blog:profile')
                 
def viewpost(request, post_id):
    if request.method == 'GET':
        try:
            post = BlogPost.objects.get(id=post_id, public=True)
        except BlogPost.DoesNotExist:
            return redirect('blog:index')
        context = {
            "post": post,
        }
        return render(request, 'blog/view.html', context)