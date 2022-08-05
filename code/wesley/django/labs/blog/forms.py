from django import forms
from django.forms import CheckboxInput, ModelForm
from .models import BlogPost

class AuthForm(forms.Form):
    username = forms.CharField(max_length=12, label="Username")
    password = forms.CharField(max_length=12, label="Password", widget=forms.PasswordInput)

class NewPost(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'public']
        widgets = {
            'public': CheckboxInput()
        }