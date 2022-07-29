from django.db import models
from django.contrib.auth.models import AbstractUser


from students.models import Student


# Create your models here.
roles = [
    ('instructor', 'Instructor'),
    ('student', 'Student'),
    ('admin', 'Admin')
]

colors = [
    ('red', 'Red'),
    ('blue', 'Blue'),
    ('yellow', 'Yellow'),
    ('orange', 'Orange'),
    ('purple', 'Purple'),
]
class User(AbstractUser):
    role = models.CharField(max_length=10, choices=roles, default='student')
    color = models.CharField(max_length=10, choices=colors, default='blue')
    student = models.OneToOneField(Student, related_name="user", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        if self.role == 'student':
            return self.student if self.student else self.username + " - No student assigned."
        else:
            return self.username