from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=40)
    height = models.FloatField()
    weight = models.FloatField()
    image_front = models.CharField(max_length=200)
    image_back = models.CharField(max_length=200)
    types = models.ManyToManyField(Type, related_name="pokemon")

    def __str__(self):
        return f"{self.number} -- {self.name}"