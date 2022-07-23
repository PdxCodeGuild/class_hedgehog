from audioop import minmax
from django.db import models
from django.forms import CharField

# Create your models here.
class Person(models.Model):
    # CharField  -> str: must have a max_length
    first_name = models.CharField(max_length=20)
    # null=True is to allow empty values in database
    # blank=True is to allow python to save empty values
    last_name = models.CharField(max_length=20, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    is_close_friend = models.BooleanField(default=False)

    # returns name in admin panel
    def __str__(self):
        return self.first_name

