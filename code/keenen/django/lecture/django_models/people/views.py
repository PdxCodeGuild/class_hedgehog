from multiprocessing import context
from django.shortcuts import render

from.models import Person

# Create your views here.
def index(request):

    if request.method == "POST":
        form = request.POST
        person = Person()
        person.first_name = form.get('first_name')
        person.last_name = form.get('last_name')
        person.age = form.get('age')
        # print(form)
        if form.get('besties'):
            person.is_close_friend = True

        person.save()

    people = Person.objects.all()

    context = {
        'people': people
    }

    return render(request, 'people/index.html', context)