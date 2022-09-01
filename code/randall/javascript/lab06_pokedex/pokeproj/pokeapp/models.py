from django.db import models

# Create your models here.


class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=50)
    height = models.FloatField()
    weight = models.FloatField()
    image_front = models.CharField(max_length=200)
    image_back = models.CharField(max_length=200)
    types = models.CharField(bug, dark, dragon, electric, fairy, fighting, fire, flying, ghost, grass, ground, ice, normal, poison, psychic, rock, steel, water)
