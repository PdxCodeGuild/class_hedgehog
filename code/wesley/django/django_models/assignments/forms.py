from django.forms import ModelForm
from django import forms
from .models import Assignment

class DateInput(forms.DateInput):
    input_type = 'date'


class NewAssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = '__all__'
        widgets = {
            'date_assigned': DateInput(), 
            'date_due': DateInput(),
        }

        