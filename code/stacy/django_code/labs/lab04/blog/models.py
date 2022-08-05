from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BlogPost(models.Model):

    title = models.CharField(max_length=24)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    public = models.BooleanField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True, upload_to='blog_images')

    def __str__(self):
        return self.title

"""
BlogPost
title (CharField)
body (TextField)
user (ForeignKey to django.contrib.auth.models.User)
public (BooleanField)
date_created (DateTimeField with auto_now_add=True)
date_edited (DateTimeField with auto_now=True)
"""