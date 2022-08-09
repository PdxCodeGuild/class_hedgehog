from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from blog.models import BlogPost

from .forms import AuthForm, CreatePost

# Create your views here.


def register(request):
    if request.method == "POST":
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
        'form': AuthForm
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
                auth.login(request.GET.get('next'))
                if next:
                    return redirect(next)
                return redirect('blog:profile')
        form.add_error(error="Invalid username or password", field="username")
        context = {
            'form': form
        }
        return render(request, 'blog/profile.html', context)

    context = {
        'form': AuthForm()
    }
    return render(request, 'blog/login.html')



@login_required
def profile(request):
    return render(request, 'blog/profile.html')




def create(request):
    if request.method == "POST":
        form = CreatePost(request.POST)
        if form.is_valid():
            post = BlogPost()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.user = request.user
            post.public = form.cleaned_data['public']

            post.save()

    return redirect('blog:profile')