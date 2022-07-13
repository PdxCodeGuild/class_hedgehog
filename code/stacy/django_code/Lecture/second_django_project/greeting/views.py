from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("test")

def greet(request, name):
    color = request.GET.get("color", "black")
    context = {
        "name": name, 
        "color": color
        }
    return render(request, "greeting/index.html", context)

def greet_form(request):
    if request.method == "POST":
        name = request.POST.get("username")
        color = request.POST.get("color")
        context = {"name": name, "color": color}
        return render(request, 'greeting/greeting.html', context)
    return render(request, 'greeting/greeting.html')