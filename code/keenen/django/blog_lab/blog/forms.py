from django import forms 
from django.forms import ModelForm
from .models import BlogPost

class AuthForm(forms.Form):
    username = forms.CharField(max_length=20, label='username')
    password = forms.CharField(max_length=20, label='password', widget=forms.PasswordInput)

class NewPost(ModelForm):
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'body',
            'public',
        ]