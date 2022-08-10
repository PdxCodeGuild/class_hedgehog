from typing import Text
from django.db import models

from django.contrib.auth.models import User

# Create your models here.

def file_route(instance, filename):
    return f'static/blog/uploads/{instance.user.id}/{filename}'

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogpost')
    public = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    image = models.FileField(upload_to=file_route, blank=True)

    def __str__(self):
        return self.title

