from django.db import models

from assignments.models import Assignment


letter_grades = [
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
    ("D", "D"),
    ("F", "F"),
]


class Student(models.Model):
    assignments = models.ManyToManyField(
        Assignment, related_name="students", blank=True)
    name = models.CharField(max_length=50)
    letter_grade = models.CharField(
        max_length=1, choices=letter_grades, default="")
    number_grade = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name
