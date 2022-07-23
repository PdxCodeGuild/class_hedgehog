from django import forms


class UpdateGroceryForm(forms.Form):
    description = forms.CharField(max_length=280)
    created_date = forms.DateField(required=False)
    completed_date = forms.DateField(required=False)
    is_completed = forms.BooleanField(required=False)


"""
from django.forms import ModelForm

class PersonForm(forms.ModelForm)
    class Meta:
        model = Person
"""