from django import forms

from .models import TodoItem

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        exclude = ['completed_date', 'created_date',]