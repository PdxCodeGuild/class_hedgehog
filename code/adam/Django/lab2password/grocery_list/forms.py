from django.forms import ModelForm
from .models import GroceryList, Item

class GroceryForm(ModelForm):
    class Meta:
        model = GroceryList
        fields = '__all__'


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

