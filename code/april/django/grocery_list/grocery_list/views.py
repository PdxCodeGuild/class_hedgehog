from django.utils import timezone
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import GroceryItem
from .forms import ItemForm

def index(request):
    items = GroceryItem.objects.all()
    if request.method == "POST":
        
        form = ItemForm(request.POST)
        if form.is_valid():
            item = GroceryItem()
            item.item_name = form.cleaned_data['item_name']

            item.save()

        return redirect('index')

    context = {
        'items': items,
        'form': ItemForm,
    }

    return render(request, 'grocery_list/index.html', context)


def completed(request, item_id):
    try:
        item = GroceryItem.objects.get(id=item_id)
    except GroceryItem.DoesNotExist:
        return redirect(reverse('index'))

    item.completed = not item.completed
    item.completed_date = timezone.now()
    item.save()
    
    return redirect(reverse('index'))


def delete(request, item_id):
    try:
        item = GroceryItem.objects.get(id=item_id)
    except GroceryItem.DoesNotExist:
        return redirect(reverse('index'))

    item.delete()

    return redirect(reverse('index'))

