from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import Person, State
from django.urls import is_valid_path, reverse
from .forms import UpdatePersonForm

# Create your views here.


# CRUD
# Create
# Read
# Update
# Delete
# List

def index(request):
# Combo of C and L
    if request.method == 'POST':
        form = request.POST
        person = Person()
        person.first_name = form.get("first_name")
        person.last_name = form.get("last_name")
        person.age = form.get("age")
        state_id = int(form.get("state"))
        state = State.objects.get(id=state_id)
        person.state = state
        if form.get("is_close_friend"):
            person.is_close_friend = True
        person.save()

    people = Person.objects.all()
    states = State.objects.all()
    context = {
        "people": people,
        "states": states
    }
    return render(request, 'people/index.html', context)

# Read
def person_detail(request, person_id):
    try:
        person = Person.objects.get(id=person_id)
    except Person.DoesNotExist:
        return HttpResponseRedirect(reverse('index'))
    
    formData = {
        "first_name": person.first_name,
        "last_name": person.last_name,
        "age": person.age,
        "is_close_friend": person.is_close_friend
    }
    context = {
        "person": person,
        "form": UpdatePersonForm(formData)
    }
    return render(request, "people/detail.html", context)

# U
def update_person(request, person_id):
    form = UpdatePersonForm(request.POST)
    if form.is_valid():
        person = Person.objects.get(id=person_id)
        person.first_name = form.cleaned_data["first_name"]
        person.last_name = form.cleaned_data["last_name"]
        person.age = form.cleaned_data["age"]
        if form.cleaned_data["is_close_friend"]:
            person.is_close_friend = True
        else:
            person.is_close_friend = False
        person.save()
    return HttpResponseRedirect(reverse("person_detail", args=(person_id,)))

# D
def delete_person(request, person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    return HttpResponseRedirect(reverse('index'))