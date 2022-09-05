from django.db import models

# class PokemonType(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=200)
    height = models.FloatField()
    weight = models.FloatField()
    image_front = models.CharField(max_length=200)
    image_back = models.CharField(max_length=200)
    # types = models.ManyToManyField(PokemonType, related_name="pokemon")
    types = models.CharField(max_length=300)

    def __str__(self):
        # return f"Name: {self.name}  Number: {self.number} Type: {self.types}"
        return self.name
