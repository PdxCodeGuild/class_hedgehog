from django.db import models

# Create your models here.

choices = [
    ("high", "High"),
    ("medium", "Medium"),
    ("low", "Low")
]

class Priority(models.Model):
    name = models.CharField(max_length=6, choices=choices, default='')

    def __str__(self):
        return self.name



class TodoItem(models.Model):
    text = models.CharField(max_length=100)
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT)
    completed_date = models.DateTimeField(blank=True, null=True)

    def  __str__(self):
        return self.text