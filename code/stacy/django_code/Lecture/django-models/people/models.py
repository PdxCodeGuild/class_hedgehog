from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=20) #CharField requires max_length
    last_name = models.CharField(max_length=20, null=True, blank=True) #null lets us have a blank field in our database, blank lets django enter an empty field, both are required for optional field
    age = models.IntegerField(null=True, blank=True)
    is_close_friend = models.BooleanField(default=False)

    def __str__(self):
        if self.last_name:
            return self.last_name + ', ' + self.first_name
        else:
            return self.first_name 



