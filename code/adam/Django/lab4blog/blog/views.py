from django.shortcuts import render
from blog.models import BlogPost, User
from .forms import BlogForm


# Create your views here.

def loginPage(request):

    context = {}
    return render(request, "blog/login_register.html", context)



def index(request):
    msg = "Turtle Island is great, so many turtles here."

    context = {
        "msg": msg
    }
    return render(request, 'blog/index.html', context)



def createPost(request):
    form = BlogForm()
    if request.method == "POST":
        form = BlogForm(request.POST)
        print(request.POST)
            
    context = {
        "form": form
    }

    return render(request, 'blog/create_post.html', context)