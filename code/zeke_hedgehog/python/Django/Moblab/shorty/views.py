from django.shortcuts import redirect, render
from .forms import ShortyForms
from .models import ShortenedURL
import string, random

# Create your views here.

def index(request):
    list = ShortenedURL.objects.all()

    context = {
        "list" : list

    }
    return render(request, 'shorty/index.html', context)


def shortyurl(request):
    form = ShortyForms() 
    if request.method == "POST":
        form = ShortyForms(request.POST)
        if form.is_valid():
            url = request.POST['url']
            code = generator()
            shorturl = ShortenedURL()
            shorturl.url = url 
            shorturl.code = code
            
            shorturl.save()
            return redirect("shorty:index")
    context = {
        'form': form
    }

    return render(request, 'shorty/create_url.html', context)
 
def generator():
    characters = string.ascii_letters + string.digits

    code = ''
    for i in range(6):
        code += random.choice(characters)

    return(code)


