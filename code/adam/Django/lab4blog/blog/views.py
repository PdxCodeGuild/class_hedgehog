from django.shortcuts import redirect, render
from blog.models import BlogPost, User
from .forms import BlogForm


# Create your views here.

def loginPage(request):

    context = {}
    return render(request, "blog/login_register.html", context)



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