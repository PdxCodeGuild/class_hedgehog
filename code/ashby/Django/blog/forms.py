from django import forms

from .models import BlogPost

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        exclude = ('user', 'date_created',)

class AuthForm(forms.Form):
    username = forms.CharField(max_length=20, label='username')
    password = forms.CharField(max_length=12, label='password' , widget=forms.PasswordInput, )