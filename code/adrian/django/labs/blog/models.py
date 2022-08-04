from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=15)
    body = models.TextField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog")
    public = models.BooleanField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title