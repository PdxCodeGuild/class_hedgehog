from django.db import models

# Create your models here.
class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=64)
    height = models.FloatField()
    weight = models.FloatField()
    image_front = models.CharField(max_length=256)
    image_back = models.CharField(max_length=256)
    types = models.CharField(max_length=256)

    def __str__(self):
        return f"No: {self.number}, Name: {self.name}, {self.types}"
