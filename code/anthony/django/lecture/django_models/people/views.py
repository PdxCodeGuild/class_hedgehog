from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Person, State
from .forms import UpdatePersonForm


# CRUD
# C - create
# R - read
# U - update
# D - delete
# L - list

# C/L
def index(request):

    if request.method == "POST":
        form = request.POST
        person = Person()
        person.first_name = form.get("first_name")
        person.last_name = form.get("last_name")
        person.age = form.get("age")

        state_id = int(form.get("state"))
        state = State.objects.get(id=state_id)
        person.state = state

        if form.get("besties"):
            person.is_close_friend = True

        person.save()

    people = Person.objects.all()
    states = State.objects.all()

    context = {
        "people": people,
        "states": states
    }
    return render(request, "people/index.html", context)


# R - Read
def person_detail(request, person_id):
    # localhost:8000/person/4
    try:
        person = Person.objects.get(id=person_id)
    except Person.DoesNotExist:
        return HttpResponseRedirect(reverse('index'))

    formData = {
        "first_name": person.first_name,
        "last_name": person.last_name,
        "age": person.age,
        "besties": person.is_close_friend
    }
    context = {
        "person": person,
        "form": UpdatePersonForm(formData)
    }
    return render(request, "people/detail.html", context)

# U - Update


def update(request, person_id):
    form = UpdatePersonForm(request.POST)
    if form.is_valid():
        person = Person.objects.get(id=person_id)
        person.first_name = form.cleaned_data['first_name']
        person.last_name = form.cleaned_data['last_name']
        person.age = form.cleaned_data['age']
        if form.cleaned_data['besties']:
            person.is_close_friend = True
        else:
            person.is_close_friend = False

        person.save()
    return HttpResponseRedirect(reverse("person_detail", args=(person_id,)))


# D - Delete
def delete(request, person_id):

    person = Person.objects.get(id=person_id)

    person.delete()

    return HttpResponseRedirect(reverse('index'))
