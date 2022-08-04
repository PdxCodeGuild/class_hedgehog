from django.db import models

# Create your models here.
class ShortenedURL(models.Model):
    url = models.URLField(max_length=200)
    code = models.CharField(max_length=200)

    def __str__(self):
        return self.url