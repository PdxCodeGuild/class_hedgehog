from django import forms

class UpdateGroceryList(forms.Form):
    description = forms.CharField(max_length=30)