from django.forms import ModelForm
from django import forms
from .models import GroceryItem


class DateInput(forms.DateInput):
    input_type = "date"


class GroceryForm(ModelForm):
    class Meta:
        model = GroceryItem
        fields = "__all__"
        widgets = {
            'date_created': DateInput(),
            'date_completed': DateInput()
        }