from django import forms

class AuthForm(forms.Form):
    username = forms.CharField(max_length=12, label="Username")
    password = forms.CharField(max_length=12, label="Password", widget=forms.PasswordInput)

class NewPost(forms.Form):
    title = forms.CharField(max_length=24)
    body = forms.CharField()
    public = forms.BooleanField(required=False)
    image = forms.ImageField(required=False, label="Upload Image")