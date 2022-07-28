from django.contrib import admin

# Register your models here.

from .models import Person, State

admin.site.register(Person)
admin.site.register(State)
