from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth

from .forms import  AuthForm, NewPost
from .models import BlogPost

def index(request):
    return render(request, 'blog/index.html')

def register(request):
    if request.method == "POST":
        form = AuthForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password']
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
                    redirect('next')
                return redirect('profile')
        form.add_error(error="Invalid username and/or password", field="username")
        context = {
            "form": form
        }
        return render(request, 'blog/login.html', context)
    context = {
        'form': AuthForm()
    }
    return render(request, 'blog/login.html', context)

@login_required
def profile(request):
    posts = BlogPost.objects.filter(user=request.user)
    context = {
        "posts": posts
    }
    return render(request, 'blog/profile.html', context)


@login_required
def create(request):
    if request.method == "POST":
        form = NewPost(request.POST)
        if form.is_valid():
            blog_post = BlogPost()
            blog_post.title = form.cleaned_data['title']
            blog_post.body = form.cleaned_data['body']
            blog_post.public = form.cleaned_data['public']
            blog_post.user = request.user
            blog_post.save()

            return redirect('profile')
        context = {
            "form": form
        }
    elif request.method == "GET":
        context = {
            "form": NewPost()
        }
    return render(request, 'blog/create.html', context)

def update(request, post_id):
    if request.method == "GET":
        try:
            blog_post = BlogPost.objects.get(id=post_id)
        except BlogPost.DoesNotExist:
            return redirect('profile')
        if request.user == blog_post.user:
            context = {
                "blog_post": blog_post,
                "form": NewPost({"title": blog_post.title, "body": blog_post.body, "public": blog_post.public})
            }
            return render(request, 'blog/update.html', context)
        else:
            return redirect('profile')
    elif request.method == "POST":
        try:
            blog_post = BlogPost.objects.get(id=post_id)
        except BlogPost.DoesNotExist:
            return redirect('profile')
        form = NewPost(request.POST)
        if form.is_valid():
            blog_post.title = form.cleaned_data['title']
            blog_post.body = form.cleaned_data['body']
            blog_post.public = form.cleaned_data['public']

            blog_post.save()
        return redirect('profile')
   
    return render(request, 'blog/update.html', context)

def delete(request, blog_id):

    pass

def blogosphere(request):
    blogs = BlogPost.objects.all()
    context = {
        "blogs": blogs
    }
    return render(request, 'blog/blogosphere.html', context)

def view_blog(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id)
    context = {
        "blog": blog
    }
    return render(request, 'blog/blogpost.html', context)


"""

Blog
Let's create a blog with a user system.

Part 1: User System
Create the following views:

Register /register/
form for creating a new user
redirect to /profile/ after registering
Login /login/
form for logging a user in
redirect to /profile/ after logging in
Profile /profile/
a protected page only logged in users can see
just show a welcome message for now
Part 2: List Blog Posts & Create Blog Post
Create the following model:

BlogPost
title (CharField)
body (TextField)
user (ForeignKey to django.contrib.auth.models.User)
public (BooleanField)
date_created (DateTimeField with auto_now_add=True)
date_edited (DateTimeField with auto_now=True)
Create the following pages:

Profile /profile/
show a list of the user's own posts, only showing the title of each
Create Post /create/
form for creating a new post
Part 3: Edit Post (optional)
Allow users to edit their BlogPosts by creating an edit page. Make sure you prevent users from editing eachother's blog posts (make sure the id for the blog post passed in via the path corresponds to a BlogPost for the logged-in User).

Edit Post /edit/<int:blogpost_id>/
form for editing an existing post
Part 4: View Other Posts (optional)
Add pages for users to browse each other's posts.

List of Posts /posts/
list posts by all users
Post Detail /posts/<int:blogpost_id>/
view a blog post
Part 5: Images (optional)
Add an ImageField to your model so each blog post can have a header image. Show a preview of this image on every post list, and the full image on a post detail.

"""
