from django.db import models

# Create your models here.


# Create your models here.
class GroceryItem(models.Model):
    #Grocery item
    grocery_item = models.CharField(max_length=25)
    # date of being added
    date_added = models.DateField(auto_now_add=True)
    #date updated
    date_updated = models.DateField(auto_now=True)
    #completed purchase of item
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return self.grocery_item