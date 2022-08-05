from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils import timezone
from django.contrib.auth.models import User
from .models import BlogPost
from .forms import BlogForm, AuthForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    context = {
        'posts': BlogPost.objects.all().filter(public=True).order_by('-date_edited')
    }
    return render(request, 'blog/home.html', context)



def register(request):
    if request.method == 'POST':
        form= AuthForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']    
            user= User.objects.create_user(username=username, password=password)
            auth.login(request, user)
            return redirect('blog:index')
        else:
            context = {'form': form}
    else:
        context = {
            'form': AuthForm()
        }

    return render(request, 'blog/register.html', context)



def login(request):
    if request.method == 'POST':
        form= AuthForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            
            if user != None:
                auth.login(request, user)
                next = request.GET.get('next')
                
                if next:
                    return redirect('next')

                return redirect('blog:profile')

        form.add_error(error='invalid login information', field='username')
        context={
            'form': form,
        }   
        
    else:
        context = {
            'form': AuthForm()
        }
    return render(request, 'blog/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('blog:index')

@login_required(login_url='blog:index')
def profile(request):
    context = {'form': BlogForm(), 'user_post': BlogPost.objects.filter(user=request.user)}
    return render(request, 'blog/profile.html', context)

@login_required(login_url='blog:index')
def create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = BlogPost()
            blog.title = form.cleaned_data['title']
            blog.body = form.cleaned_data['body']
            blog.public = form.cleaned_data['public']
            blog.user = request.user
            blog.date_created = timezone.now()
            blog.image=form.cleaned_data['image']
            blog.image = form.cleaned_data['image']
            blog.save()
            return redirect('blog:profile')
        else:
            context={
                'form' : form,
            }
            return render(request, 'blog/profile.html', context)

@login_required(login_url='blog:index')
def edit(request, post_id):
    if request.method == 'GET':
        try:
            post = BlogPost.objects.get(id=post_id)
            if post.user == request.user:
                context ={
                    'post': post,
                    'form': BlogForm(instance=post)
                }
            
                return render(request, 'blog/edit.html', context)
    
        except BlogPost.DoesNotExist:
            return redirect('blog:profile')   
    
    elif request.method == 'POST':
        try:
            post = BlogPost.objects.get(id=post_id)
        except BlogPost.DoesNotExist:
            pass

        form = BlogForm(request.POST, request.FILES, instance = post)
        if form.is_valid():
            form.save()
    return redirect('blog:profile')

@login_required(login_url='blog:index')
def delete(request, post_id):
    try:
        post = BlogPost.objects.get(id=post_id)
        if request.user == post.user:
            post.delete()
            
    except BlogPost.DoesNotExist:
        pass
    return redirect('blog:profile')

def detail(request, post_id):
    try:
        post = BlogPost.objects.get(id=post_id)
        if post.public == True or post.user == request.user:
            context = {
                'post': post,
            }
            return render(request, 'blog/detail.html', context)
            
    except BlogPost.DoesNotExist:
        pass
    return redirect('blog:profile')
