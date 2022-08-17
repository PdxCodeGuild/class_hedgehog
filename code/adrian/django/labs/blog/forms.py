from django import forms
from django.forms import ModelForm
from .models import BlogPost

class AuthForm(forms.Form):
    username = forms.CharField(max_length=15, label="username")
    password = forms.CharField(max_length=15, label="password", widget=forms.PasswordInput)


class CreatePost(ModelForm):
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'body',
        ]
