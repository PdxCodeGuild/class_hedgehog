from multiprocessing import context
from django.shortcuts import render
from django.http import HttpRequest
from .models import Person

# Create your views here.

def index(request):

    if request.method == 'POST':
        form = request.POST
        person = Person()
        person.first_name = form.get("first_name")
        person.last_name = form.get("last_name")
        person.age = form.get("age")
        if form.get("is_close_friend"):
            person.is_close_friend = True
        person.save()

    people = Person.objects.all()
    context = {
        "people": people
    }
    return render(request, 'people/index.html', context)