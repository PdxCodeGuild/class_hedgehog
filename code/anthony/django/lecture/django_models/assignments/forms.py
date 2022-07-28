from django.forms import ModelForm
from django import forms
from .models import Assignment


class DateInput(forms.DateInput):
    input_type = "date"


class NewAssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = "__all__"
        widgets = {
            'date_assigned': DateInput(),
            'date_due': DateInput()
        }


"""
class NewAssignmentForm(forms.Form):
    title = forms.CharField(label="Title")
    description = forms.CharField(widget=forms.Textarea)
    date_assigned = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}))
    date_due = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
"""
