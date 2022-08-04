from django import forms


# use to register and login
class AuthForm(forms.Form):
    username = forms.CharField(max_length=12, label="Username")
    password = forms.CharField(max_length=16, label="Password", widget=forms.PasswordInput)