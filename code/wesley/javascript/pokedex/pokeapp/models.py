from django.db import models

# Create your models here.

class PokemonType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    height = models.FloatField()
    weight = models.FloatField()
    image_front = models.CharField(max_length=100)
    image_back = models.CharField(max_length=100)
    types = models.ManyToManyField(PokemonType, related_name='pokemon', blank=True)

    def __str__(self):
        return self.name
