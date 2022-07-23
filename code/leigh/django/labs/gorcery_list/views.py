from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import GroceryItem
from django.urls import reverse
from .forms import UpdateItemForm

def index(request):

    if request.method == "POST":
        grocery_item = GroceryItem()
        grocery_item.description = request.POST.get("description")
        
        grocery_item.save()

    grocery_list = GroceryItem.objects.all()

    context = {
        "grocery_list": grocery_list
    }
    return render(request, "grocery_list/index.html", context)


def complete(request, grocery_item_id):
    grocery_item = GroceryItem.objects.get(id=grocery_item_id)
    grocery_item.completed = not grocery_item.completed
    
    grocery_item.save()
    return HttpResponseRedirect(reverse("index"))


def delete(request, grocery_item_id):
    grocery_item = GroceryItem.objects.get(id=grocery_item_id)
    grocery_item.delete()
    return HttpResponseRedirect(reverse('index'))