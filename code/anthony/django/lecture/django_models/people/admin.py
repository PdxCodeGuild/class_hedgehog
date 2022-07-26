from django.contrib import admin

from .models import Person, State

admin.site.register(State)
admin.site.register(Person)
