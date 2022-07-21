from django import forms


class password_form(forms.Form):
    
    char_num = forms.CharField(label='enter the number of characters')