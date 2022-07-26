from django.contrib import admin
from .models import Person, State
# Register your models here.

admin.site.register(State)
admin.site.register(Person)
