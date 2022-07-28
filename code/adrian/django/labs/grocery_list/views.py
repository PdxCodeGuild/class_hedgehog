from django.shortcuts import render
from django.http import HttpResponse
from .models import GroceryItem
from .forms import UpdateGroceryList
# Create your views here.

def index(request):
    
    if request.method == "POST":
        grocery_item = GroceryItem()
        grocery_item.description = request.POST.get("description")

        grocery_item.save()

    grocery_list = GroceryItem.objects.all()
    context = {
        "grocery_list": grocery_list
    }

    return render(request, 'grocery_list/index.html', context)
