from django.forms import ModelForm
from .models import TodoItem


class TodoForm(ModelForm):
    class Meta:
        model = TodoItem
        fields = '__all__'