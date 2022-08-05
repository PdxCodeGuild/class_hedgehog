from django.shortcuts import render

# Create your views here.

def loginPage(requests):

    context = {}
    return render(requests, "blog/login_register.html", context)



def index(requests):
    msg = "Turtle Island is great, so many turtles here."

    context = {
        "msg": msg
    }
    return render(requests, 'blog/index.html', context)