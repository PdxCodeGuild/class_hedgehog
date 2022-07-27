from django.db import models
from django.forms import BooleanField

# Create your models here.

class GroceryItem(models.Model):
    description = models.CharField(max_length=280)
    created_date = models.DateField(auto_now_add=True, null=True, blank=True)
    completed_date = models.DateField(auto_now=True, null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description
        

"""
GroceryItem which contains a text description, a created date, a completed date, and a boolean representing whether it was completed.

The user should be presented with an input field and a button (in a form). When the clicks the button, it should save the data to the server and show the newly-added item in the list. The user should be presented with a list of incomplete items and a list of complete items. THe user should be able to mark an item complete/incomplete and be able to delete an item.



class Person(models.Model):
    # CharField -> Str: Must have a max_length
    first_name = models.CharField(max_length=20)
    # null=True is to allow empty values in database
    # blank=True is to allow python to save empty values
    last_name = models.CharField(max_length=20, null=True, blank=True)
    # models.PositiveIntegerField()
    age = models.IntegerField(null=True, blank=True)
    is_close_friend = models.BooleanField(default=False)
"""