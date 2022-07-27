from django.forms import ModelForm
from .models import TodoItem

class NewTodoForm(ModelForm):
    class Meta:
        model = TodoItem
        fields = ("description",)
