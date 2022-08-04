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
    return render(request, 'blog/home.html')


#TODO make register
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


#TODO make login route
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

#TODO make profile route
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
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = BlogPost()
            blog.title = form.cleaned_data['title']
            blog.body = form.cleaned_data['body']
            blog.public = form.cleaned_data['public']
            blog.user = request.user
            blog.date_created = timezone.now()
            blog.save()
            return redirect('blog:profile')
        else:
            context={
                'form' : form,
            }
            return render(request, 'blog/profile.html', context)
            