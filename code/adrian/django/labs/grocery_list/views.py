from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
import grocery_list
from grocery_list.forms import GroceryForm
from .models import GroceryItem
# Create your views here.

def index(request):
    groceries = GroceryItem.objects.all()

    context = {
       "groceries": groceries,
    }

    return render(request, 'grocery_list/index.html', context)


def create_item(request):
    if request.method == "POST":
        form = GroceryForm(request.POST)
        if form.is_valid():
            item = GroceryItem()
            item.description = form.cleaned_data['description']
            item.completed = form.cleaned_data['completed']

            date_created = form.cleaned_data['date_created']
            date_completed = form.cleaned_data['date_completed']

            if date_created:
                item.date_created = date_created
            if date_completed:
                item.date_completed = date_completed
            
            item.save()
            url = reverse('grocery_list:index')
            return redirect(url)
        else:
            context = {
                'form': form
            }
            return render(request, 'grocery_list/create.html', context)
    
    context = {
        'form': GroceryForm()
    }
    return render(request, 'grocery_list/create.html', context)


def completed(request, item_id):
    item = GroceryItem.objects.get(id=item_id)
    item.save()

    return HttpResponseRedirect(reverse('grocery_list:index'))



def delete_item(request, item_id):
    item = GroceryItem.objects.get(id=item_id)
    item.delete()

    return HttpResponseRedirect(reverse('grocery_list:index'))
