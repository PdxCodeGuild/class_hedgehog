from django.forms import ModelForm
from .models import ShortenedURL




class ShortyForms(ModelForm):
    class Meta:
        model = ShortenedURL
        fields = "__all__"