from django.db import models

# Create your models here.

class GroceryItem(models.Model):
    description = models.CharField(max_length=30)

    date_created = models.DateField(null=True, blank=True)

    date_completed = models.DateField(null=True, blank=True)

    completed = models.BooleanField(default=False)

def __str__(self):
    return self.description