
from django.db import models

priority_levels = [
    ('HIGH', 'high'),
    ('MEDIUM', 'medium'),
    ('LOW', 'low'),
]

class Priority(models.Model):
    priority = models.CharField(choices=priority_levels, max_length=6, default='')

    def __str__(self):
        return self.priority

class TodoItem(models.Model):
    todo_item = models.CharField(max_length=200)
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True)
    # completed_date = models.DateTimeField(blank=True, null=True)
    completed_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.todo_item