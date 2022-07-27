from unittest.util import _MAX_LENGTH
from django.db import models

from assignments.models import Assignment

letter_grades = [
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
    ("D", "D"),
    ("F", "F")
]
# Create your models here.
class Student(models.Model):
    assignments = models.ManyToManyField(Assignment, related_name="student", blank=True)
    name = models.CharField(max_length=20)
    letter_grade = models.CharField(max_length=1, choices=letter_grades, default = "")
    number_grade = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name