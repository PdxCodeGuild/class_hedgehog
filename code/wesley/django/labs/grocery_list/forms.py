from email.policy import default
from django import forms 

class AddItemForm(forms.Form):
    desc = forms.CharField(max_length=200 )
    created_date = forms.DateField()

class UpdateItemForm(forms.Form):
    comp_date = forms.DateField(required=False)
    complete = forms.BooleanField(required=False)