from django.forms import ModelForm
from .models import GroceryList, Item

class StartList(ModelForm):
    class Meta:
        model = GroceryList
        fields = '__all__'


# class Add_Item(ModelForm):