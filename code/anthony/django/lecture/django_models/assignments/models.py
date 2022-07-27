from django.db import models


class Assignment(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    # auto_now=True to auto populate
    date_assigned = models.DateField(blank=True, null=True)
    date_due = models.DateField()

    def __str__(self):
        return self.title
