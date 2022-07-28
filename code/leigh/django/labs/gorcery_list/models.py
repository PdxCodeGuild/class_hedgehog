from django.db import models

# Create your models here.
class GroceryItem(models.Model):
    description = models.TextField(max_length=20)
    # null is allowed and django allows no value entered
    created_date = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description