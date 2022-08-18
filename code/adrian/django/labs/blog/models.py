from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog")
    public = models.BooleanField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title