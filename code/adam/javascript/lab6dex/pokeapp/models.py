from django.db import models
from PIL import Image
from io import BytesIO

# Create your models here.



class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=50)
    height = models.FloatField()
    weight = models.FloatField()
    image_front = models.CharField(max_length=300)
    image_back = models.CharField(max_length=300)
    # types = models.CharField()


    class Meta:
        ordering = ('number',)

    def __str__(self):
        return self.name

    def get_image(self):
        if self.image_front:
            return 'http://127.0.0.1:8000' + self.image_front.url
        return ""
    # def get_thumbnail