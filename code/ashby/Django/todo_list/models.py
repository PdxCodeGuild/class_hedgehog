from itertools import filterfalse
from django.db import models

# Create your models here.
#priority_list = [('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low'),]

class Priority(models.Model):
    priority = models.CharField(max_length=10)

    def __str__(self):
        return self.priority


class TodoItem(models.Model):
    name = models.CharField( max_length = 50)
    description = models.TextField()
    priority = models.ForeignKey(Priority, on_delete = models.PROTECT)
    created_date = models.DateTimeField(auto_now_add = True)
    completed_date = models.DateTimeField(default = None, null = True, blank=True)

    def __str__(self):
        return self.name