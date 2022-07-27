from django.db import models
from django.forms import DateField

# Create your models here.

class Assignment(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    date_assigned = models.DateField(blank=True, null=True)
    date_due = models.DateField()

    def __str__(self):
        return self.title