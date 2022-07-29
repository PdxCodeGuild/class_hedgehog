from dataclasses import fields
from django import forms

from .models import GroceryItem

class GroceryForm(forms.ModelForm):

    class Meta:
        model = GroceryItem
        exclude = ['purchased', ]

