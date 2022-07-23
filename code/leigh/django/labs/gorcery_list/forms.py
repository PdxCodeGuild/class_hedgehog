from django import forms

class UpdateItemForm(forms.Form):
    description = forms.CharField(max_length=20)