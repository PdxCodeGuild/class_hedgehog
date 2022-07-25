from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import GroceryList, Item
from .forms import StartList
# Create your views here.

def index(request):
    list = GroceryList.objects.all()
    item = Item.objects.all()
    
    context = {
        'list': list,
        'items': item, 
    }

    return render(request, "grocery_list/grocery.html", context)

def create_list(request):
    form = StartList()
    if request.method == 'POST':
        form = StartList(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groceries')
    context = {
        "form": form
    }
    return render(request, 'grocery_list/create_list.html', context)
    
    # form = StartList()

# def add_item(request, pk):
