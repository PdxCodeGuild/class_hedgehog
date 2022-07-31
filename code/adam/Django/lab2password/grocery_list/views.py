from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import GroceryList, Item
from .forms import StartList
# Create your views here.


def index(request):
    list = GroceryList.objects.all()
    
    
    context = {
        'lists': list,
         
    }

    return render(request, "grocery_list/grocery.html", context)



def grocery_list(request, pk):
    list = GroceryList.objects.get(id=pk)
    items = list.item_set.all()
    print(items)
    context = {"grocery_list": list,
                "items": items,
        }

    return render(request, 'grocery_list/grocery_list.html', context)


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


def update_list(request, pk):
    list = GroceryList.objects.get(id=pk)
    form = StartList(instance=list)
    if request.method == 'POST':
        form = StartList(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return redirect('groceries')

    context = {"form": form}        
    return render(request, 'grocery_list/create_list.html', context)

def delete_list(request, pk):
    list = GroceryList.objects.get(id=pk)
    if request.method == 'POST':
        list.delete()
        return redirect('groceries')
    
    return render(request, 'grocery_list/delete.html', {'obj': list})

    # form = StartList()

# def add_item(request, pk):
