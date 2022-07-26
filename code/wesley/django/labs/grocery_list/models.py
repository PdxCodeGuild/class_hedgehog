from datetime import datetime
from django.db import models

# Create your models here.
class GroceryItem(models.Model):
    desc = models.CharField(max_length=200)
    created_date = models.DateField(null=True, blank=True)
    comp_date = models.DateField(null=True, blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.desc

    