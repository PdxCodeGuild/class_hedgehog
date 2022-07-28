from django.db import models

class Priority(models.Model):
    priority = models.CharField(max_length=10)
    
    def __str__(self):
        return self.priority
        
class TodoItem(models.Model):
    description = models.TextField()
    completed_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT)

    def __str__(self):
        return self.description

