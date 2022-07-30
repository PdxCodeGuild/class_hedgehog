from django.db import models

# Create your models here.

class ShortenedURL():

    code = models.CharField(max_length=6)
    url = models.URLField(max_length=240)
    pass
