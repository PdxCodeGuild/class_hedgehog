from django.db import models

# Create your models here.


class State(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Person(models.Model):
    # CharField -> Str: Must have a max_length
    first_name = models.CharField(max_length=20)
    # null=True is to allow empty values in database
    # blank=True is to allow python to save empty values
    last_name = models.CharField(max_length=20, null=True, blank=True)
    # models.PositiveIntegerField()
    age = models.IntegerField(null=True, blank=True)
    is_close_friend = models.BooleanField(default=False)
    state = models.ForeignKey(
        State, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.first_name.lower()
