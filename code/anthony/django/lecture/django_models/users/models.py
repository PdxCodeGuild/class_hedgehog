from django.db import models
from django.contrib.auth.models import AbstractUser

from students.models import Student

roles = [
    ('instructor', 'Instructor'),
    ('student', 'Student'),
    ('admin', 'Admin')
]

colors = [
    ('red', 'red'),
    ('blue', 'blue'),
    ('green', 'green'),
    ('yellow', 'yellow'),
    ('orange', 'orange'),
    ('purple', 'purple'),
]


class User(AbstractUser):
    role = models.CharField(max_length=10, choices=roles, default='student')
    color = models.CharField(max_length=10, choices=colors, default='blue')
    student = models.OneToOneField(
        Student, related_name="user", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        if self.role == 'student':
            return self.student if self.student else self.username + " - No student assigned."
        else:
            return self.username


# user = User.objects.get(id=1)
# user.role
# user.color
# user.student.assignments.get(title="lab 01")
