from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    image = models.URLField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
    public = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    