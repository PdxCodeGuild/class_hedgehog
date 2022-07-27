from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import GroceryItem
from .forms import UpdateGroceryForm


# Create your views here.
"""
Let's create a simple grocery list app.
This can be done with a single app called grocery_list and model called GroceryItem which contains a text description, a created date, a completed date, and a boolean representing whether it was completed.

The user should be presented with an input field and a button (in a form). When the clicks the button, it should save the data to the server and show the newly-added item in the list. The user should be presented with a list of incomplete items and a list of complete items. THe user should be able to mark an item complete/incomplete and be able to delete an item.

"""
# Create, List
def index(request):
    
    if request.method == "POST":
        form = request.POST
        grocery_item = GroceryItem()
        grocery_item.description = form.get("description")
        # grocery_item.created_date = form.get("created_date")
        # grocery_item.completed_date = form.get("completed_date")
        if form.get("is_completed"):
            grocery_item.is_completed = True
        else:
            grocery_item.is_completed = False
        grocery_item.save()

    grocery_items = GroceryItem.objects.all()

    context = {
        "grocery_items": grocery_items
    }
    return render(request, "grocery_list/index.html", context)

# Read
def item_detail(request, item_id):
    try:
        grocery_item = GroceryItem.objects.get(id=item_id)
    except GroceryItem.DoesNotExist:
        return HttpResponseRedirect(reverse('index'))
    formData = {
        "description": grocery_item.description,
        "created_date": grocery_item.created_date,
        "completed_date": grocery_item.completed_date,
        "is_completed": grocery_item.is_completed
    }
    if not formData["is_completed"]:
        formData["completed_date"] = None
    context = {
        "grocery_item": grocery_item,
        "form": UpdateGroceryForm(formData)
    }
    return render(request, 'grocery_list/detail.html', context)

# Update
def update(request, item_id):
    form = UpdateGroceryForm(request.POST)
    if form.is_valid():
        grocery_item = GroceryItem.objects.get(id=item_id)
        grocery_item.description = form.cleaned_data["description"]
        grocery_item.created_date = form.cleaned_data["created_date"]
        if form.cleaned_data['is_completed']:
            grocery_item.is_completed = True
            grocery_item.completed_date = form.cleaned_data["completed_date"]
        else:
            grocery_item.is_completed = False

        grocery_item.save()
    return HttpResponseRedirect(reverse("item_detail", args=(item_id,)))

# Delete
def delete(request, item_id):
    grocery_item = GroceryItem.objects.get(id=item_id)
    grocery_item.delete()
    return HttpResponseRedirect(reverse('index'))
# in html file, two separate lists, one for complete and one for incomplete
