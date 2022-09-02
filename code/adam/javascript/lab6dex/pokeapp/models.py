from django.db import models

# Create your models here.
class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=50)
    height = models.FloatField()
    wight = models.FloatField()
    image_front = models.CharField(max_length=300)
    image_back = models.CharField(max_length=300)
    # types = models.CharField()


    def __str__(self):
        return self.name
