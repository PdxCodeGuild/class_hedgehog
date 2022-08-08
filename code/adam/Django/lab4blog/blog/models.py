from django.db import models
from django.contrib.auth.models import User




class BlogPost(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField(max_length=300, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    public = models.BooleanField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title



class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    body = models.TextField(max_length=250)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.body[:50]