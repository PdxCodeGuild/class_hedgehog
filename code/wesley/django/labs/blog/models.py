from django.db import models
from django.contrib.auth.models import User
from django.forms import CheckboxInput


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=24)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='blogposts')
    public = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    
    def __str__ (self):
        return self.title