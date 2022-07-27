from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import GroceryItem
from .forms import AddItemForm, UpdateItemForm

# Create your views here.
def index(request):
    form_add = AddItemForm(request.POST)
    if request.method == 'POST':
        groc_item = GroceryItem()
        if form_add.is_valid():
            groc_item.desc = form_add.cleaned_data['desc']
            groc_item.created_date = form_add.cleaned_data['created_date']
            groc_item.save()
            form_add = AddItemForm()
    else:
        form_add = AddItemForm()


    item_list = GroceryItem.objects.filter(complete=False)
    comp_item_list = GroceryItem.objects.filter(complete=True)
    context = {
        "form_add": form_add,
        "item_list": item_list,
        "comp_item_list": comp_item_list,
    }

    return render(request, 'grocery_list/index.html', context)

def update(request, item_id):
    try:
        item = GroceryItem.objects.get(id=item_id)
    except GroceryItem.DoesNotExist:
        return HttpResponseRedirect(reverse('index'))

    form_update = UpdateItemForm(request.POST)
    if form_update.is_valid():
        item = GroceryItem.objects.get(id=item_id)
        item.comp_date = form_update.cleaned_data['comp_date']
        if form_update.cleaned_data['complete']:
            item.complete = True
        else:
            item.complete = False

        item.save()
        
    formData = {
        'comp_date': item.comp_date,
        'complete': item.complete
    }

    context = {
        'form_update': UpdateItemForm(formData),
        'item': item
    }

    return render(request, 'grocery_list/detail.html', context)