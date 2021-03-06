from django import forms

class UpdatePersonForm(forms.Form):
    first_name = forms.CharField(max_length=20, required=False)
    last_name = forms.CharField(max_length=20, required=False)
    age = forms.IntegerField(min_value=0, max_value=140, required=False)
    besties = forms.BooleanField(required=False)