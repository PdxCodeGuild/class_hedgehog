from django.db import models

# Create your models here.

priority = [
    ('high', 'High'),
    ('medium', 'Medium'),
    ('low', 'Low')
]

class Priority(models.Model):
    name = models.CharField(max_length=6, choices=priority, default='')

    def __str__(self):
        return self.name

class ToDoItem(models.Model):
    text = models.CharField(max_length=50)
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT, blank=True, null=True)
    completed_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.text