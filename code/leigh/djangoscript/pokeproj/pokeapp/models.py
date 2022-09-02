from django.db import models

# Create your models here.

class Types(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=20)
    height = models.FloatField()
    weight = models.FloatField()
    image_front = models.CharField(max_length=200)
    image_back = models.CharField(max_length=200)
    types = models.ManyToManyField(Types, related_name="pokemon", blank=True, null=True)

    def __str__(self):
        return self.name

