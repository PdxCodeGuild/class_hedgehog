from django import forms
from django.forms import ModelForm
from .models import BlogPost


# use to register and login
class AuthForm(forms.Form):
    username = forms.CharField(max_length=12, label="Username")
    password = forms.CharField(max_length=16, label="Password", widget=forms.PasswordInput)

class NewBlogPost(ModelForm):
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'body',
            'public',
        ]

