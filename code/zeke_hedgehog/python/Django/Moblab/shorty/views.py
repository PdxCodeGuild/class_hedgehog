from django.shortcuts import redirect, render
from .forms import ShortyForms
from .models import ShortenedURL

# Create your views here.

def index(request):
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'shorty/index.html', context)


def shortyurl(request):

    forms = ShortyForms() 
    if request.method == "POST":
        form = ShortyForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    context = {
        'forms': forms
    }

    return render(request, 'shorty/index.html', context)
