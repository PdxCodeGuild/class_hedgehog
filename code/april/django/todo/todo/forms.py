from django import forms
from django.forms import ModelForm
from .models import TodoItem

class DateInput(forms.DateInput):
    input_type = "date"

class TodoForm(ModelForm):
    class Meta:
        model = TodoItem
        fields = '__all__'
        widgets = {
            'completed_date':DateInput(), 
        }