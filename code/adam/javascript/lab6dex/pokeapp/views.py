from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.
def poke_app(request):
    msg = "Hello Turtle Island!"

    context = {
        "msg": msg
    }
    return render(request, 'pokeapp/index.html', context)