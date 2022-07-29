from django.forms import ModelForm
from django import forms
from .models import ToDoItem

class DateInput(forms.DateInput):
    input_type = 'date'

class NewToDoForm(ModelForm):
    class Meta:
        model = ToDoItem
        fields = '__all__'
        widgets = {
            'completed_date': DateInput(),
        }