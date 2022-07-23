
# add this to your app folder
from django import forms

choices = [
    ("high", "High"),
    ("medium", "Medium"),
    ("low", "Low")
]

class TodoForm(forms.Form):
    todo_text = forms.CharField(label="Enter todo text")
    priority = forms.ChoiceField(label="Priority", choices=choices)


# import this file into views.py
# from .forms import TodoForm

# pass the form into the views.py context
# "form": TodoForm()