
from django.db import models

status_choices = [
    ( "Complete", "Complete"),
    ( "Incomplete", "Incomplete")
]
# completed = models.BooleanField(choices=status_choices, default="Incomplete") 

# Create your models here.
class GroceryList(models.Model):
    details = models.CharField(max_length=200, null=True, blank=True)
    completed = models.CharField(choices=status_choices, max_length=15, default="Incomplete") 
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.details
        

class Item(models.Model):
    grocerylist = models.ForeignKey(GroceryList, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveSmallIntegerField(default=1, null=True)

    def __str__(self):
        return self.item_name