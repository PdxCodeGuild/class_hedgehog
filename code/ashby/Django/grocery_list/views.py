from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import GroceryForm
from .models import GroceryItem
# Create your views here.


# Read I suppose
def index(request):

    if request.method == "POST":
        form = GroceryForm(request.POST or None)
        if form.is_valid():
            form.save()
            

    groceries = GroceryItem.objects.all()
    context = {
    'form': GroceryForm, 
    'groceries': groceries,
    }

    return render(
        request,
        'grocery_list/index.html',
        context
    )

def details(request, grocery_id):
    
    try:
        grocery = GroceryItem.objects.get(id=grocery_id)
    except GroceryItem.DoesNotExist:
            return HttpResponse(reverse('index'))

    context = { 'grocery': grocery}

    return render(request, 'grocery_list/detail.html', context)



def delete(request, grocery_id):
    grocery = GroceryItem.objects.get(id=grocery_id)
    
    grocery.delete()

    return HttpResponseRedirect(reverse('grocery'))


def complete(request, grocery_id):
    
    grocery = GroceryItem.objects.get(id=grocery_id)
    grocery.purchased = not grocery.purchased
    grocery.save()


    return HttpResponseRedirect(reverse('grocery'))
   


