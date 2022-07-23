from django.db import models

# Create your models here.

class GroceryItem(models.Model):
    description = models.TextField(max_length=30)

    date_created = models.DateField()

    date_completed = models.DateField()

    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description